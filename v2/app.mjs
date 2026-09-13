import {createClient} from '@supabase/supabase-js';
import {config} from './config.mjs';
import {t,locale} from './i18n.mjs';
import {readState,writeState,clearState,mayEdit,escapeHTML as e,compressPhoto} from './store.mjs';
const db=createClient(config.url,config.key,{auth:{flowType:'pkce',detectSessionInUrl:true,persistSession:true}});
const root=document.querySelector('#app');
const params=new URLSearchParams(location.search);
let demo=params.get('demo')==='1',session=null,account=null,state=null,catalog=[],view='today',selected=null,filter='',search='',syncing=false,toastTimer,photoDraft=null,photoDraftURL=null;
const urls=new Map();
const icons={leaf:'<path d="M20 4C8 3 3 8 5 15c7 4 15-1 15-11Z"/><path d="M4 21 15 9"/>',today:'<path d="m3 11 9-8 9 8v10H3Z"/><path d="M9 21v-8h6v8"/>',garden:'<path d="M12 21V10M12 14C4 15 3 9 3 5c8-1 10 4 9 9ZM12 10c-1-6 3-9 9-8 0 6-3 9-9 8Z"/>',ask:'<path d="M21 11c0 5-4 8-9 8H6l-4 3V11a9 9 0 0 1 19 0Z"/><path d="M7 10h10M7 14h6"/>',settings:'<circle cx="12" cy="8" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3"/>',camera:'<path d="M3 7h4l2-3h6l2 3h4v14H3Z"/><circle cx="12" cy="14" r="4"/>'};
const icon=name=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${icons[name]||icons.leaf}</svg>`;
const btn=(label,action,classes='',attrs='')=>`<button type="button" class="btn ${classes}" data-action="${action}" ${attrs}>${label}</button>`;
const field=(id,label,control)=>`<div class="field"><label for="${id}">${label}</label>${control}</div>`;
const input=(id,label,value='',type='text')=>field(id,label,`<input id="${id}" type="${type}" value="${e(value)}" maxlength="${id==='question'?4000:120}">`);
const textArea=(id,label,value='')=>field(id,label,`<textarea id="${id}" maxlength="4000">${e(value)}</textarea>`);
const val=id=>document.getElementById(id)?.value?.trim()??'';
const checked=id=>document.getElementById(id)?.checked??false;
const uuid=()=>crypto.randomUUID();
const activeGarden=()=>state?.gardens.find(g=>g.id===state.gardenId);
const plants=()=>state.plants.filter(p=>p.garden_id===state.gardenId);
const envs=()=>state.environments.filter(x=>x.garden_id===state.gardenId);
const tasks=()=>state.tasks.filter(x=>x.garden_id===state.gardenId);
const species=p=>catalog.find(s=>s.key===p?.species_key);
const envName=id=>state.environments.find(x=>x.id===id)?.name||'';
const own=()=>activeGarden()?.owner_id===account;
const edit=()=>demo||mayEdit(state,account);
const pending=()=>state?.outbox?.length||0;
function notify(text){clearTimeout(toastTimer);document.querySelector('#toast').textContent=text;toastTimer=setTimeout(()=>document.querySelector('#toast').textContent='',6500);}
function fresh(){return {gardens:[],gardenId:null,members:[],invitations:[],environments:[],plants:[],tasks:[],consultations:[],preferences:{weekly_tasks:true,funfacts_per_week:2},capabilities:{},outbox:[],photos:{},lastSync:null};}
function demoState(){
 const s=fresh(),g=uuid(),env=uuid();s.gardens=[{id:g,owner_id:'demo',name:'Jardín de ejemplo',city:'Montevideo',timezone:'America/Montevideo'}];s.gardenId=g;s.environments=[{id:env,garden_id:g,name:'Jardín del fondo'}];
 const chosen=catalog;
 s.plants=chosen.map((p,i)=>({id:uuid(),garden_id:g,environment_id:env,name:p.name,species_key:p.key,notes:'',demo_photo:p.photo}));
 s.tasks=s.plants.slice(0,2).map((p,i)=>({id:uuid(),garden_id:g,plant_id:p.id,title:['Revisar cómo está el sustrato','Observar hojas y brotes'][i],instructions:'Cuidado de ejemplo para explorar la experiencia. Revisá las condiciones reales de tu planta antes de actuar.',due_date:new Date().toISOString().slice(0,10),status:'active',version:1}));return s;
}
async function persist(){await writeState(account,state);}
async function mutate(ops,change){
 const backup=structuredClone(state);change();if(!demo)state.outbox.push(...ops.map(op=>({...op,operationId:uuid()})));
 try{await persist();}catch(err){state=backup;throw new Error('No hay espacio para guardar. Liberá espacio antes de continuar.');}
 render();notify(demo?t('savedLocal'):navigator.onLine?'Guardado; sincronizando…':t('savedLocal'));
 if(!demo&&navigator.onLine)void sync();
}
async function sync(){
 if(demo||syncing||!navigator.onLine||!session)return;syncing=true;
 try{
  while(state.outbox.length){
   const op=state.outbox[0];let result;
   if(op.kind==='photo'){
    result=await db.storage.from('garden-photos').upload(op.path,state.photos[op.path],{contentType:'image/jpeg',upsert:false});
    if(result.error&&/already exists|Duplicate/i.test(result.error.message)){
     // A lost response may leave a completed upload. Recheck authorized access.
     const check=await db.storage.from('garden-photos').download(op.path);if(!check.error)result={error:null};
    }
   }else if(op.kind==='update'){
    result=await db.from(op.table).update(op.row).eq('id',op.id).eq('version',op.expected).select();
    if(!result.error&&!result.data.length){
     const check=await db.from(op.table).select('*').eq('id',op.id).maybeSingle();
     if(check.data&&check.data.version===op.expected+1&&Object.entries(op.row).every(([k,v])=>check.data[k]===v))result={data:[check.data]};
     else throw new Error(t('conflict'));
    }
   }else if(op.kind==='prefs')result=await db.from('preferences').upsert(op.row);
   else {
    result=await db.from(op.table).insert(op.row);
    if(result.error?.code==='23505'){
     const check=await db.from(op.table).select('*').eq('id',op.row.id).maybeSingle();
     if(check.data&&Object.entries(op.row).every(([k,v])=>check.data[k]===v))result={error:null};
    }
   }
   if(result.error)throw result.error;
   state.outbox.shift();await persist();
  }
  await refresh();state.lastSync=new Date().toISOString();await persist();
 }catch(err){state.syncError=err.message||t('error');await persist().catch(()=>{});notify(state.syncError);}
 finally{syncing=false;render();}
}
async function refresh(){
 const [gs,ms,ivs,ps,cap]=await Promise.all([db.from('gardens').select('*'),db.from('garden_members').select('*'),db.from('invitations').select('*'),db.from('preferences').select('*').maybeSingle(),db.rpc('my_capabilities')]);
 for(const r of [gs,ms,ivs,ps,cap])if(r.error)throw r.error;
 state.gardens=gs.data;state.members=ms.data;state.invitations=ivs.data;state.preferences=ps.data||state.preferences;state.capabilities=cap.data;
 if(!state.gardens.some(x=>x.id===state.gardenId))state.gardenId=state.gardens[0]?.id||null;
 const results=await Promise.all(['environments','plants','tasks','consultations'].map(table=>db.from(table).select('*')));
 results.forEach((r,i)=>{if(r.error)throw r.error;state[['environments','plants','tasks','consultations'][i]]=r.data;});
 // Purge data for gardens no longer visible, including device copies of photos.
 const allowed=new Set(state.gardens.map(g=>g.id));for(const path of Object.keys(state.photos))if(!allowed.has(path.split('/')[0])){delete state.photos[path];if(urls.has(path)){URL.revokeObjectURL(urls.get(path));urls.delete(path);}}
 for(const p of state.plants){if(p.photo_path&&!state.photos[p.photo_path]){const photo=await db.storage.from('garden-photos').download(p.photo_path);if(!photo.error)state.photos[p.photo_path]=photo.data;}}
 delete state.syncError;
}
function photo(p){
 if(p?.photo_path&&state.photos[p.photo_path]){if(!urls.has(p.photo_path))urls.set(p.photo_path,URL.createObjectURL(state.photos[p.photo_path]));return urls.get(p.photo_path);}
 return p?.demo_photo||'';
}
function brand(){return `<div class="brand">${icon('leaf')}${t('brand')}<span style="color:#8ea175">.</span></div>`;}
function login(){root.innerHTML=`<div class="login"><div class="login-copy">${brand()}<span class="eyebrow">CUIDAR TAMBIÉN ES DISFRUTAR</span><h1>${t('loginTitle')}</h1><p class="muted">${t('loginBody')}</p><div class="stack gap8">${btn('G &nbsp; '+t('google'),'login','primary')}${btn(t('explore'),'demo','quiet')}<p class="small muted">${t('loginHint')}</p></div><footer>${t('install')}</footer></div><div class="login-image" role="img" aria-label="Jardín lleno de plantas"></div></div>`;}
function shell(body){
 const g=activeGarden();const status=pending()?`${pending()} ${t('pending')}`:navigator.onLine?t('online'):t('offline');
 root.innerHTML=`<aside class="sidebar">${brand()}<div class="garden-switch"><span class="eyebrow">TU ESPACIO VERDE</span><select id="garden-switch" aria-label="Elegir jardín">${state.gardens.map(x=>`<option value="${x.id}" ${x.id===state.gardenId?'selected':''}>${e(x.name)}</option>`).join('')}</select><span class="small muted">${e(g?.city||'')}</span></div><nav class="navigation" aria-label="Navegación principal">${['today','garden','ask','settings'].map(x=>`<button class="nav ${view===x?'active':''}" data-view="${x}" ${view===x?'aria-current="page"':''}>${icon(x)}${t(x)}</button>`).join('')}</nav><div class="sidebar-foot"><div class="line"></div><p class="small muted">Crecer lleva tiempo.<br>Disfrutá el camino.</p><div class="row"><span class="avatar">${demo?'J':e(session?.user.email?.slice(0,1).toUpperCase())}</span><span class="small">${demo?'Explorando':e(session?.user.email?.split('@')[0])}</span></div></div></aside><main class="main"><div class="topbar"><span class="date muted">${new Intl.DateTimeFormat(locale,{weekday:'long',day:'numeric',month:'long'}).format(new Date())}</span><div class="mobile-brand">${brand()}</div><button class="btn quiet small" data-action="sync" aria-label="${t('sync')}"><span class="dot"></span>${syncing?'Sincronizando…':e(status)}</button></div>${demo?`<div class="demo-line">${t('demo')}</div>`:''}${state.syncError?`<div class="notice error">${e(state.syncError)}</div><div class="spacer"></div>`:''}${body}</main>`;
}
function head(title,sub,action=''){return `<header class="page-head"><div><h1>${title}</h1><p class="muted">${sub}</p></div>${action}</header>`;}
function card(p){const sp=species(p),src=photo(p);return `<button class="plant-card" data-plant="${p.id}">${src?`<img src="${e(src)}" alt="${e(p.name)}" loading="lazy">`:`<div class="photo-placeholder">❧</div>`}<div class="card-content"><h3>${e(p.name)}</h3><p class="small muted">${e(sp?.scientific||t('pendingIdentity'))}</p><div class="meta"><span>${e(envName(p.environment_id))}</span><span>↗</span></div></div></button>`;}
function taskRow(task){const p=state.plants.find(p=>p.id===task.plant_id);return `<article class="task"><button class="check ${task.status==='done'?'done':''}" data-task="${task.id}" ${!edit()?'disabled':''} aria-label="${task.status==='done'?'Reabrir':'Completar'}: ${e(task.title)}">${task.status==='done'?'✓':''}</button><div><p class="task-title">${e(task.title)}</p><small>${e(p?.name||activeGarden()?.name)}${task.due_date?' · '+e(task.due_date):''}</small>${task.instructions?`<details class="small muted"><summary>Cómo hacerlo</summary><p>${e(task.instructions)}</p></details>`:''}${task.status!=='done'&&edit()?`<div class="task-actions">${btn(t('later'),'snooze','quiet',`data-id="${task.id}"`)}</div>`:''}</div></article>`;}
function home(){
 const list=plants(),todo=tasks().filter(x=>x.status!=='done'),sp=species(list[0]);
 return head(t('welcome'),t('intro'),edit()?btn('+ '+t('add'),'add','primary'):'')+`<section class="hero"><div class="hero-copy"><span class="eyebrow">${t('week')}</span><h2>${todo.length?'Pequeños cuidados.<br>Grandes cambios.':t('noTasks')}</h2><p class="muted">${todo.length?`${todo.length} cuidados para acompañar tu jardín.`:t('noTasksBody')}</p>${btn(todo.length?'Ver mis cuidados':t('garden'),todo.length?'scroll-tasks':'garden','primary')}</div><div class="hero-photo" style="background-image:url('https://images.unsplash.com/photo-1585598117791-876ce25c1884?auto=format&fit=crop&w=1200&q=80')"><span class="badge">${e(activeGarden()?.name)}</span></div></section><div class="dashboard-grid"><section class="panel" id="care-list"><div class="section-head"><h2>${t('next')}</h2><span class="badge">${todo.length}</span></div>${todo.length?todo.slice(0,5).map(taskRow).join(''):`<div class="empty"><p>${t('noTasksBody')}</p>${edit()?btn('+ '+t('addTask'),'new-task','soft'):''}</div>`}<div class="row stat"><strong>${tasks().filter(x=>x.status==='done').length}</strong><span class="small muted">${t('completed')}</span></div></section><aside class="panel fact"><span class="eyebrow">${t('curiosity')}</span><span class="sprig">❧</span><h3>${e(sp?.name||'Aprendé de tu jardín')}</h3><p>${e(sp?.funfact||'Cuando confirmes la especie de tu primera planta, vas a encontrar curiosidades sobre ella acá.')}</p>${list[0]?btn(t('details')+' ↗','detail','quiet',`data-id="${list[0].id}"`):''}</aside></div><div class="spacer"></div><div class="section-head"><h2>${t('yourPlants')}</h2>${btn('Ver todas →','garden','quiet')}</div><div class="cards">${list.slice(0,3).map(card).join('')}</div>`;
}
function garden(){let list=plants().filter(p=>(!filter||p.environment_id===filter)&&(!search||(p.name+' '+(species(p)?.name||'')).toLowerCase().includes(search.toLowerCase())));return head(t('collection'),`${plants().length} ${t('plants')} · ${envs().length} ${t('environments')}`,edit()?btn('+ '+t('add'),'add','primary'):'')+`<div class="filters">${btn(t('all'),'filter',!filter?'soft':'',`data-id=""`)}${envs().map(x=>btn(e(x.name),'filter',filter===x.id?'soft':'',`data-id="${x.id}"`)).join('')}</div>${input('search',t('search'),search)}<div class="spacer"></div>${list.length?`<div class="cards">${list.map(card).join('')}</div>`:`<div class="panel empty"><h2>${plants().length?'No encontramos esa planta.':t('emptyGarden')}</h2>${edit()?btn('+ '+t('add'),'add','primary'):''}</div>`}`;}
function detail(){const p=state.plants.find(x=>x.id===selected);if(!p)return garden();const sp=species(p);return `${btn('← '+t('back'),'garden','quiet')}<div class="spacer"></div>`+head(e(p.name),e(envName(p.environment_id)))+`<div class="detail-layout"><div>${photo(p)?`<img class="detail-photo" src="${e(photo(p))}" alt="${e(p.name)}">`:'<div class="photo-placeholder">❧</div>'}<div class="spacer"></div><div class="panel"><h3>${t('notes')}</h3><p>${e(p.notes||t('noNotes'))}</p></div></div><div class="stack"><p class="eyebrow">${e(sp?.scientific||t('pendingIdentity'))}</p>${sp?`<div class="care-grid"><div class="panel"><span class="eyebrow">${t('light')}</span><p>${e(sp.light)}</p></div><div class="panel"><span class="eyebrow">${t('water')}</span><p>${e(sp.water)}</p></div></div><div class="panel"><h3>${t('pruning')}</h3><p>${e(sp.pruning)}</p></div><div class="panel fact"><span class="eyebrow">${t('curiosity')}</span><p>${e(sp.funfact)}</p></div>`:`<div class="notice">${t('noInfo')}</div>`}${edit()?`<div class="row">${btn(t('ask'),'ask','primary',`data-id="${p.id}"`)}${btn('+ '+t('addTask'),'new-task','',`data-id="${p.id}"`)}</div>`:''}<div>${tasks().filter(x=>x.plant_id===p.id).map(taskRow).join('')}</div></div></div>`;}
function add(){return `${btn('← '+t('back'),'garden','quiet')}<div class="spacer"></div>`+head(t('photo'),t('photoBody'))+`<div class="editor-layout"><div><label class="upload">${photoDraftURL?`<img src="${photoDraftURL}" alt="Vista previa de la planta">`:icon('camera')+`<strong>${t('choosePhoto')}</strong><span class="small muted">JPG, PNG o WebP</span>`}<input id="photo" type="file" accept="image/jpeg,image/png,image/webp" aria-label="${t('choosePhoto')}"></label><p class="small muted" style="margin-top:12px">Una foto clara, con hojas y tallo visibles.</p></div><div class="stack">${input('plant-name',t('name'))}${field('species',t('species'),`<select id="species"><option value="">${t('unknown')}</option>${catalog.map(x=>`<option value="${x.key}">${e(x.name)} — ${e(x.scientific)}</option>`).join('')}</select>`)}${field('environment',t('environment'),`<select id="environment">${envs().map(x=>`<option value="${x.id}">${e(x.name)}</option>`).join('')}<option value="new">+ ${t('newEnvironment')}</option></select>`)}${field('environment-name',t('envName'),`<input id="environment-name" list="environment-options" maxlength="80" placeholder="Interior, Balcón, Jardín del fondo…"><datalist id="environment-options"><option>Interior</option><option>Balcón</option><option>Jardín del frente</option><option>Jardín del fondo</option></datalist>`)}${textArea('plant-note',t('note'))}<label class="row small"><input type="checkbox" id="identify">${t('identify')}</label>${!config.aiEnabled?`<div class="notice">${t('aiPending')}</div>`:''}${btn(t('save')+' mi planta','save-plant','primary')}</div></div>`;}
function ask(){const qs=state.consultations.filter(x=>x.garden_id===state.gardenId);return head(t('askTitle'),t('askBody'))+`<div class="setting-columns"><section class="panel stack">${!config.aiEnabled?`<div class="notice">La IA todavía no está conectada. Podés dejar consultas pendientes, pero aún no se procesan.</div>`:''}${field('question-plant',t('garden'),`<select id="question-plant"><option value="">Mi jardín en general</option>${plants().map(x=>`<option value="${x.id}" ${selected===x.id?'selected':''}>${e(x.name)}</option>`).join('')}</select>`)}${textArea('question',t('question'))}${edit()?btn(t('send'),'save-question','primary'):`<p class="notice">Tu acceso es de solo lectura.</p>`}</section><section class="panel"><h2>${t('questions')}</h2>${qs.length?qs.map(q=>`<article class="query"><span class="badge">${q.status==='answered'?t('answer'):t('waiting')}</span><p>${e(q.question)}</p>${q.answer?`<div class="notice">${e(q.answer)}</div>`:''}</article>`).join(''):`<div class="empty muted">${t('noQuestions')}</div>`}</section></div>`;}
function newTask(){return head(t('addTask'),'Un recordatorio sencillo, para hacerlo a tu ritmo.')+`<div class="panel stack" style="max-width:650px">${input('task-title',t('taskTitle'))}${field('task-plant',t('yourPlants'),`<select id="task-plant"><option value="">Todo el jardín</option>${plants().map(p=>`<option value="${p.id}" ${p.id===selected?'selected':''}>${e(p.name)}</option>`).join('')}</select>`)}${input('task-date',t('taskDate'),new Date().toISOString().slice(0,10),'date')}${textArea('task-instructions','Cómo hacerlo (opcional)')}<div class="row">${btn(t('save'),'save-task','primary')}${btn(t('cancel'),'today','quiet')}</div></div>`;}
function settings(){return head(t('preferences'),'Elegí cómo compartir y acompañar tu jardín.')+`<div class="setting-columns"><section class="panel stack"><h2>Notificaciones</h2><label class="row"><input id="weekly" type="checkbox" ${state.preferences.weekly_tasks?'checked':''}>${t('weekly')}</label>${field('frequency',t('frequency'),`<select id="frequency">${[0,1,2,7].map(n=>`<option value="${n}" ${state.preferences.funfacts_per_week===n?'selected':''}>${n===0?'Desactivadas':n===7?'Una por día':n+' por semana'}</option>`).join('')}</select>`)}${btn(t('save'),'save-prefs','primary')}<p class="notice">${t('notificationsPending')}</p><div class="line"></div><h3>Este dispositivo</h3><p class="small muted">${state.lastSync?'Última sincronización: '+e(new Date(state.lastSync).toLocaleString(locale)):t('savedLocal')}. Las fotos guardadas quedan disponibles sin conexión.</p>${btn(t('sync'),'sync')}<div>${state.outbox.map(op=>`<div class="pending-row"><span class="small">${e(op.kind)} · ${e(op.row?.name||op.row?.title||op.table||t('photos'))}</span></div>`).join('')}</div>${state.syncError&&pending()?btn(t('discard'),'discard','quiet'):''}${btn(t('logout'),'logout','quiet')}</section><section class="panel stack"><h2>${t('people')}</h2><p class="small muted">${own()?'Invitá con su correo Google. Elegís qué puede hacer cada persona.':'El dueño administra los permisos del jardín.'}</p>${own()?`${input('invite-email',t('inviteEmail'),'','email')}${field('invite-role','Permiso',`<select id="invite-role"><option value="viewer">${t('viewer')}</option><option value="editor">${t('editor')}</option></select>`)}${btn(t('invite'),'invite','primary')}`:''}<div class="member"><strong>${t('owner')}</strong><span>${e(activeGarden()?.name)}</span></div>${state.members.filter(m=>m.garden_id===state.gardenId).map(m=>`<div class="member"><span>Miembro ${e(m.user_id.slice(0,8))}</span><span>${m.role==='editor'?t('editor'):t('viewer')}</span>${own()?btn('Quitar','remove-member','quiet',`data-id="${m.user_id}"`):''}</div>`).join('')}${state.invitations.filter(i=>i.garden_id===state.gardenId&&!i.accepted_at).map(i=>`<div class="member"><span>${e(i.email)}<br><small>${i.role==='editor'?t('editor'):t('viewer')} · invitación pendiente</small></span>${own()?btn('Copiar enlace','copy-invite','quiet',`data-id="${i.id}"`):''}${own()?btn('Revocar','revoke-invite','quiet',`data-id="${i.id}"`):''}</div>`).join('')}${state.capabilities.admin?`<div class="line"></div><h2>${t('admin')}</h2>${input('license-email','Correo del cliente','','email')}<div class="row">${btn('Activar','activate-license','primary')}${btn('Suspender','suspend-license')}</div>`:''}</section></div>`;}
function gate(){return head(t('awaiting'),state.capabilities.licensed?'Dale un nombre a tu espacio verde.':t('awaitingBody'))+`<div class="panel stack" style="max-width:650px">${state.capabilities.licensed?`${input('garden-name',t('gardenName'),'Mi jardín')}${input('garden-city',t('city'))}${btn(t('createGarden'),'create-garden','primary')}`:''}${state.invitations.filter(i=>!i.accepted_at).map(i=>`<div class="notice row between"><span>Te invitaron a compartir un jardín · ${i.role==='editor'?t('editor'):t('viewer')}</span>${btn(t('accept'),'accept-invite','primary',`data-id="${i.id}"`)}</div>`).join('')}${btn(t('logout'),'logout','quiet')}</div>`;}
function render(){if(!account||!state){login();return;}if(!activeGarden()){shell(gate());return;}const screens={today:home,garden,detail,add,ask,settings,'new-task':newTask};shell((screens[view]||home)());}
function navigate(next,id=null){if(photoDraftURL&&next!=='add'){URL.revokeObjectURL(photoDraftURL);photoDraftURL=null;photoDraft=null;}view=next;if(id!==null)selected=id;render();window.scrollTo(0,0);}
async function savePlant(){
 if(!edit())throw new Error('Acceso de solo lectura.');if(!photoDraft)throw new Error('Elegí una foto para comenzar.');
 const name=val('plant-name');if(!name)throw new Error('Escribí un nombre para tu planta.');
 let environmentId=val('environment');const newName=val('environment-name');if(environmentId==='new'&&!newName)throw new Error('Dale un nombre al ambiente.');
 const gid=state.gardenId,pid=uuid(),path=`${gid}/${pid}/${uuid()}.jpg`,ops=[],newEnv=environmentId==='new'?{id:uuid(),garden_id:gid,name:newName}:null;
 if(newEnv){environmentId=newEnv.id;ops.push({table:'environments',kind:'insert',row:newEnv});}
 ops.push({kind:'photo',path});
 const p={id:pid,garden_id:gid,environment_id:environmentId,name,species_key:val('species')||null,notes:val('plant-note'),photo_path:path};ops.push({kind:'insert',table:'plants',row:p});
 const q=checked('identify')?{id:uuid(),garden_id:gid,plant_id:pid,question:'Identificar la especie de esta planta a partir de su foto.',...(demo?{}:{author_id:account})}:null;
 if(q)ops.push({kind:'insert',table:'consultations',row:q});const blob=photoDraft;
 await mutate(ops,()=>{if(newEnv)state.environments.push(newEnv);state.plants.push(p);state.photos[path]=blob;if(q)state.consultations.push({...q,status:'pending'});});navigate('detail',pid);
}
async function changeTask(id,snooze=false){if(!edit())return;const task=state.tasks.find(x=>x.id===id);if(!task)return;const patch=snooze?{status:'snoozed',due_date:new Date(Date.now()+7*86400000).toISOString().slice(0,10)}:{status:task.status==='done'?'active':'done'};const expected=task.version;await mutate([{kind:'update',table:'tasks',id,row:patch,expected}],()=>Object.assign(task,patch,{version:expected+1}));}
async function action(name,node){
 if(name==='login'&&!config.googleEnabled){notify('El acceso con Google está pendiente de configuración. Podés explorar el jardín de ejemplo.');return;}
 if(name==='login'){const {error}=await db.auth.signInWithOAuth({provider:'google',options:{redirectTo:new URL('./',location.href).href}});if(error)throw error;return;}
 if(name==='demo'){location.search='?demo=1';return;}
 if(['today','garden','ask','detail','settings','new-task'].includes(name)){navigate(name,node.dataset.id||null);return;}
 if(name==='add'){navigate('add');return;}if(name==='scroll-tasks'){document.querySelector('#care-list')?.scrollIntoView({behavior:'smooth'});return;}
 if(name==='filter'){filter=node.dataset.id;render();return;}
 if(name==='save-plant'){await savePlant();return;}
 if(name==='sync'){if(demo){notify('Este jardín de ejemplo se guarda en tu dispositivo.');return;}await sync();return;}
 if(name==='snooze'){await changeTask(node.dataset.id,true);return;}
 if(name==='save-task'){
  if(!edit())throw new Error('Acceso de solo lectura.');const title=val('task-title');if(!title)throw new Error('Escribí el cuidado que querés recordar.');
  const task={id:uuid(),garden_id:state.gardenId,plant_id:val('task-plant')||null,title,instructions:val('task-instructions'),due_date:val('task-date')||null,status:'active',version:1};
  await mutate([{kind:'insert',table:'tasks',row:task}],()=>state.tasks.push(task));navigate('today');return;
 }
 if(name==='save-question'){
  if(!edit())throw new Error('Acceso de solo lectura.');const question=val('question');if(!question)throw new Error('Escribí tu consulta.');
  const q={id:uuid(),garden_id:state.gardenId,plant_id:val('question-plant')||null,question,...(demo?{}:{author_id:account})};await mutate([{kind:'insert',table:'consultations',row:q}],()=>state.consultations.push({...q,status:'pending'}));return;
 }
 if(name==='save-prefs'){const row={weekly_tasks:checked('weekly'),funfacts_per_week:Number(val('frequency')),...(demo?{}:{user_id:account})};await mutate([{kind:'prefs',row}],()=>state.preferences={...state.preferences,...row});return;}
 if(name==='logout'){
  if(pending())throw new Error(t('signoutPending'));if(!demo&&!navigator.onLine)throw new Error('Conectate para cerrar la sesión de forma segura.');
  if(!demo){const {error}=await db.auth.signOut();if(error)throw error;}await clearState(account);for(const url of urls.values())URL.revokeObjectURL(url);urls.clear();location.href='./';return;
 }
 if(name==='discard'){if(!confirm('¿Descartar el primer cambio pendiente? Si una carga depende de él, también podría requerir revisión.'))return;state.outbox.shift();await persist();await sync();return;}
 if(demo){notify('Las invitaciones y licencias se habilitan en tu jardín real.');return;}
 if(!navigator.onLine)throw new Error(t('offlineFirst'));
 if(name==='create-garden'){
  const gardenName=val('garden-name'),city=val('garden-city');if(!gardenName||!city)throw new Error('Completá nombre y ciudad.');
  const {data,error}=await db.from('gardens').insert({name:gardenName,city,timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,owner_id:account}).select().single();if(error)throw error;state.gardenId=data.id;await refresh();await persist();navigate('add');return;
 }
 if(name==='invite'){
  const email=val('invite-email').toLowerCase();if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))throw new Error('Escribí un correo válido.');
  const {error}=await db.from('invitations').insert({garden_id:state.gardenId,email,role:val('invite-role')});if(error)throw error;await refresh();await persist();render();notify('Invitación creada. Copiá el enlace para compartirlo.');return;
 }
 if(name==='copy-invite'){await navigator.clipboard.writeText(new URL('./?invite='+node.dataset.id,location.href).href);notify('Enlace copiado. Solo puede aceptarlo el correo invitado.');return;}
 if(name==='accept-invite'){const {data,error}=await db.rpc('accept_invitation',{invite_id:node.dataset.id});if(error)throw error;state.gardenId=data;await refresh();await persist();navigate('garden');return;}
 if(name==='remove-member'){const {error}=await db.from('garden_members').delete().eq('garden_id',state.gardenId).eq('user_id',node.dataset.id);if(error)throw error;await refresh();await persist();render();return;}
 if(name==='revoke-invite'){const {error}=await db.from('invitations').delete().eq('id',node.dataset.id);if(error)throw error;await refresh();await persist();render();return;}
 if(name==='activate-license'||name==='suspend-license'){const email=val('license-email').toLowerCase();if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))throw new Error('Escribí un correo válido.');const {error}=await db.from('licenses').upsert({email,active:name==='activate-license'});if(error)throw error;notify(name==='activate-license'?'Licencia activada.':'Licencia suspendida.');return;}
}
root.addEventListener('click',async event=>{
 const node=event.target.closest('button');if(!node)return;
 if(node.dataset.view){navigate(node.dataset.view);return;}if(node.dataset.plant){navigate('detail',node.dataset.plant);return;}
 node.disabled=true;try{if(node.dataset.task)await changeTask(node.dataset.task);else if(node.dataset.action)await action(node.dataset.action,node);}catch(err){notify(err.message||t('error'));}finally{if(node.isConnected)node.disabled=false;}
});
root.addEventListener('change',async event=>{
 const el=event.target;
 if(el.id==='garden-switch'){state.gardenId=el.value;filter='';selected=null;await persist();navigate('garden');}
 if(el.id==='photo'&&el.files[0]){try{photoDraft=await compressPhoto(el.files[0]);if(photoDraftURL)URL.revokeObjectURL(photoDraftURL);photoDraftURL=URL.createObjectURL(photoDraft);const image=el.parentElement.querySelector('img');if(image)image.src=photoDraftURL;else{const im=document.createElement('img');im.src=photoDraftURL;im.alt='Vista previa de la planta';el.parentElement.prepend(im);for(const x of [...el.parentElement.children])if(x!==im&&x!==el)x.remove();}}catch(err){notify(err.message);}}
 if(el.id==='search'){search=el.value;render();}
});
window.addEventListener('online',()=>void sync());
window.addEventListener('offline',()=>render());
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')void sync();});
async function boot(){
 try{
  catalog=await fetch('./catalog.json').then(r=>{if(!r.ok)throw new Error('No se pudo cargar el catálogo.');return r.json();});
  if('serviceWorker'in navigator)await navigator.serviceWorker.register('./sw.js',{scope:'./'}).catch(()=>{});
  if(demo){account='demo';state=await readState(account)||demoState();await persist();render();return;}
  const result=await db.auth.getSession();session=result.data.session;
  if(!session){login();return;}account=session.user.id;state=await readState(account)||fresh();render();
  if(navigator.onLine)await sync();
 }catch(err){root.innerHTML=`<div class="empty"><h1>No pudimos abrir tu jardín.</h1><p>${e(err.message)}</p><a class="btn" href="./">Reintentar</a></div>`;}
}
void boot();
