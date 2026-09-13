-- Jardineando: a separate shared-garden application; no legacy data is imported.
create schema if not exists private;
revoke all on schema private from public;
grant usage on schema private to authenticated;
create table private.platform_admins (user_id uuid primary key references auth.users(id));
create table public.licenses (
 email text primary key check(email = lower(trim(email))),
 active boolean not null default true,
 created_at timestamptz not null default now()
);
create table public.gardens (
 id uuid primary key default gen_random_uuid(),
 owner_id uuid not null default auth.uid() references auth.users(id),
 name text not null check(length(name) between 1 and 100),
 city text not null default '', timezone text not null default 'America/Montevideo',
 created_at timestamptz not null default now()
);
create index on public.gardens(owner_id);
create table public.garden_members (
 garden_id uuid not null references public.gardens(id) on delete cascade,
 user_id uuid not null references auth.users(id),
 role text not null check(role in ('viewer','editor')),
 primary key(garden_id,user_id)
);
create index on public.garden_members(user_id);
create table public.invitations (
 id uuid primary key default gen_random_uuid(), garden_id uuid not null references public.gardens(id) on delete cascade,
 email text not null check(email=lower(trim(email))), role text not null check(role in ('viewer','editor')),
 expires_at timestamptz not null default now()+interval '7 days', accepted_at timestamptz,
 unique(garden_id,email)
);
create table public.environments (
 id uuid primary key default gen_random_uuid(), garden_id uuid not null references public.gardens(id) on delete cascade,
 name text not null check(length(name) between 1 and 80), exposure text not null default 'unknown',
 unique(id,garden_id)
);
create index on public.environments(garden_id);
create table public.plants (
 id uuid primary key default gen_random_uuid(), garden_id uuid not null references public.gardens(id) on delete cascade,
 environment_id uuid not null, name text not null check(length(name) between 1 and 120),
 species_key text, notes text not null default '' check(length(notes)<=4000),
 photo_path text, created_at timestamptz not null default now(),
 unique(id,garden_id),
 foreign key(environment_id,garden_id) references public.environments(id,garden_id)
);
create index on public.plants(garden_id);
create index on public.plants(environment_id,garden_id);
create table public.tasks (
 id uuid primary key default gen_random_uuid(), garden_id uuid not null references public.gardens(id) on delete cascade,
 plant_id uuid, title text not null check(length(title) between 1 and 200),
 instructions text not null default '' check(length(instructions)<=4000), due_date date,
 status text not null default 'active' check(status in ('active','done','snoozed')),
 version integer not null default 1, updated_by uuid references auth.users(id),
 updated_at timestamptz not null default now(),
 foreign key(plant_id,garden_id) references public.plants(id,garden_id)
);
create index on public.tasks(garden_id,due_date);
create index on public.tasks(plant_id,garden_id);
create index on public.tasks(updated_by);
create table public.consultations (
 id uuid primary key default gen_random_uuid(), garden_id uuid not null references public.gardens(id) on delete cascade,
 plant_id uuid, author_id uuid not null default auth.uid() references auth.users(id),
 question text not null check(length(question) between 1 and 4000),
 status text not null default 'pending' check(status in ('pending','processing','answered','needs_photo','failed')),
 answer text, created_at timestamptz not null default now(),
 foreign key(plant_id,garden_id) references public.plants(id,garden_id)
);
create index on public.consultations(garden_id);
create index on public.consultations(plant_id,garden_id);
create index on public.consultations(author_id);
create table public.preferences (
 user_id uuid primary key default auth.uid() references auth.users(id),
 weekly_tasks boolean not null default true,
 funfacts_per_week integer not null default 2 check(funfacts_per_week in (0,1,2,7)),
 locale text not null default 'es', timezone text not null default 'America/Montevideo'
);

-- These internal helpers must read membership without triggering recursive RLS.
-- Their only authority is auth.uid(); callers cannot impersonate another user.
create function private.current_email() returns text language sql stable security definer set search_path=''
 as $$ select lower(email) from auth.users where id=auth.uid() and email_confirmed_at is not null $$;
create function private.is_admin() returns boolean language sql stable security definer set search_path=''
 as $$ select auth.uid() is not null and exists(select 1 from private.platform_admins where user_id=auth.uid()) $$;
create function private.licensed() returns boolean language sql stable security definer set search_path=''
 as $$ select auth.uid() is not null and exists(select 1 from public.licenses where email=private.current_email() and active) $$;
create function private.garden_access(gid uuid, access_kind text default 'read') returns boolean
 language sql stable security definer set search_path='' as $$
 select auth.uid() is not null and exists(
  select 1 from public.gardens g join auth.users u on u.id=g.owner_id
  join public.licenses l on l.email=lower(u.email) and l.active
  where g.id=gid and (g.owner_id=auth.uid() or (access_kind<>'owner' and exists(
   select 1 from public.garden_members m where m.garden_id=g.id and m.user_id=auth.uid()
   and (access_kind='read' or (access_kind='write' and m.role='editor'))))))
 $$;
revoke all on all functions in schema private from public;
grant execute on function private.current_email(),private.is_admin(),private.licensed(),private.garden_access(uuid,text) to authenticated;

alter table public.licenses enable row level security;
alter table public.gardens enable row level security;
alter table public.garden_members enable row level security;
alter table public.invitations enable row level security;
alter table public.environments enable row level security;
alter table public.plants enable row level security;
alter table public.tasks enable row level security;
alter table public.consultations enable row level security;
alter table public.preferences enable row level security;
revoke all on public.licenses,public.gardens,public.garden_members,public.invitations,public.environments,public.plants,public.tasks,public.consultations,public.preferences from anon,authenticated;
grant select,insert,update,delete on public.licenses to authenticated;
create policy licenses_read on public.licenses for select to authenticated using(email=private.current_email() or private.is_admin());
create policy licenses_admin on public.licenses for all to authenticated using(private.is_admin()) with check(private.is_admin());
grant select,insert on public.gardens to authenticated;
grant update(name,city,timezone) on public.gardens to authenticated;
create policy gardens_read on public.gardens for select to authenticated using(private.garden_access(id));
create policy gardens_create on public.gardens for insert to authenticated with check(owner_id=auth.uid() and private.licensed());
create policy gardens_update on public.gardens for update to authenticated using(private.garden_access(id,'owner')) with check(private.garden_access(id,'owner'));
grant select,insert,delete on public.garden_members to authenticated;
grant update(role) on public.garden_members to authenticated;
create policy members_read on public.garden_members for select to authenticated using(private.garden_access(garden_id));
create policy members_owner on public.garden_members for all to authenticated using(private.garden_access(garden_id,'owner')) with check(private.garden_access(garden_id,'owner'));
grant select,insert,delete on public.invitations to authenticated;
create policy invitations_read on public.invitations for select to authenticated using(private.garden_access(garden_id,'owner') or (email=private.current_email() and accepted_at is null and expires_at>now()));
create policy invitations_owner on public.invitations for all to authenticated using(private.garden_access(garden_id,'owner')) with check(private.garden_access(garden_id,'owner') and accepted_at is null);
grant select,insert on public.environments,public.plants,public.tasks,public.consultations to authenticated;
grant update(name,exposure) on public.environments to authenticated;
grant update(name,species_key,notes,photo_path,environment_id) on public.plants to authenticated;
grant update(status,due_date,version) on public.tasks to authenticated;
create policy env_read on public.environments for select to authenticated using(private.garden_access(garden_id));
create policy env_write on public.environments for all to authenticated using(private.garden_access(garden_id,'write')) with check(private.garden_access(garden_id,'write'));
create policy plants_read on public.plants for select to authenticated using(private.garden_access(garden_id));
create policy plants_write on public.plants for all to authenticated using(private.garden_access(garden_id,'write')) with check(private.garden_access(garden_id,'write'));
create policy tasks_read on public.tasks for select to authenticated using(private.garden_access(garden_id));
create policy tasks_write on public.tasks for all to authenticated using(private.garden_access(garden_id,'write')) with check(private.garden_access(garden_id,'write'));
create policy consultations_read on public.consultations for select to authenticated using(private.garden_access(garden_id));
create policy consultations_create on public.consultations for insert to authenticated with check(private.garden_access(garden_id,'write') and author_id=auth.uid() and status='pending' and answer is null);
grant select,insert,update on public.preferences to authenticated;
create policy prefs_self on public.preferences for all to authenticated using(user_id=auth.uid()) with check(user_id=auth.uid());

create function private.task_version() returns trigger language plpgsql set search_path='' as $$
begin
 new.version=old.version+1; new.updated_at=now(); new.updated_by=auth.uid(); return new;
end $$;
create trigger task_version before update on public.tasks for each row execute function private.task_version();

-- Atomic email-bound acceptance; caller cannot choose the resulting role/user.
create function private.accept_invitation(invite_id uuid) returns uuid language plpgsql security definer set search_path='' as $$
declare inv public.invitations; gid uuid;
begin
 if auth.uid() is null or private.current_email() is null then raise exception 'authentication_required'; end if;
 select * into inv from public.invitations where id=invite_id for update;
 if inv.id is null or inv.email<>private.current_email() or inv.accepted_at is not null or inv.expires_at<=now() then raise exception 'invitation_unavailable'; end if;
 if not exists(select 1 from public.gardens g join auth.users u on u.id=g.owner_id join public.licenses l on l.email=lower(u.email) and l.active where g.id=inv.garden_id) then raise exception 'garden_inactive'; end if;
 insert into public.garden_members(garden_id,user_id,role) values(inv.garden_id,auth.uid(),inv.role)
 on conflict(garden_id,user_id) do update set role=excluded.role;
 update public.invitations set accepted_at=now() where id=inv.id;
 return inv.garden_id;
end $$;
revoke all on function private.accept_invitation(uuid),private.task_version() from public;
grant execute on function private.accept_invitation(uuid) to authenticated;
create function public.accept_invitation(invite_id uuid) returns uuid language sql security invoker set search_path=''
 as $$ select private.accept_invitation(invite_id) $$;
revoke all on function public.accept_invitation(uuid) from public;
grant execute on function public.accept_invitation(uuid) to authenticated;
create function public.my_capabilities() returns jsonb language sql security invoker set search_path=''
 as $$ select jsonb_build_object('admin',private.is_admin(),'licensed',private.licensed()) $$;
revoke all on function public.my_capabilities() from public;
grant execute on function public.my_capabilities() to authenticated;

insert into storage.buckets(id,name,public,file_size_limit,allowed_mime_types)
 values('garden-photos','garden-photos',false,2097152,array['image/jpeg','image/webp','image/png']);
create policy garden_photos_read on storage.objects for select to authenticated
 using(bucket_id='garden-photos' and private.garden_access((storage.foldername(name))[1]::uuid));
create policy garden_photos_insert on storage.objects for insert to authenticated
 with check(bucket_id='garden-photos' and private.garden_access((storage.foldername(name))[1]::uuid,'write'));
-- Unique filenames: no client overwrite/delete permissions for photos.
