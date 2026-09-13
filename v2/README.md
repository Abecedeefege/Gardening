# Jardineando v2 — preview

Open `/app/?demo=1` to review the interface with local example data. Add a photo, assign an environment, inspect species information, and record tasks. Demo changes are stored only on the device.

Build: `npm ci && npm run build:v2`. Generated assets live in `docs/app/`; the existing site is preserved.

This is a review preview, not a production release. Google OAuth needs a client ID/secret configured in Supabase and an allowed redirect URL. AI identification and push delivery are not connected. Their UI states explicitly describe this. Invitations and licensing require authenticated accounts; security and multi-device synchronization need end-to-end validation before release. Database migrations are in `supabase/migrations/`.

Never place a Supabase service-role key or Google client secret in frontend code.

Preview catalog is generic, not an export of the personal garden. Public example photography: Fujiphilm (https://unsplash.com/photos/sfxK-xw4bo4), Annie Spratt (https://unsplash.com/photos/NrflUuJJK0I), Thimo van Leeuwen (https://unsplash.com/photos/nz08m1BF8Io).
