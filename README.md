# tetra

Multi-tenant SaaS ERP. **Milestone 1: authentication foundation.**

## What ships in this milestone

- Tenants + users with email / password authentication.
- Tenant-scoped sessions.
- Real password hashing (bcrypt, via Masonite 5's `Authenticates` trait).
- Real signup, login, logout.
- Real password reset via email link (24h expiry, single-use).
- Real email verification via signed link.
- Tenant boundary enforced on every authenticated request.

No ERP modules, no subdomain routing, no RBAC beyond "owner", no social login, no billing.

## Stack

- **Python** 3.14
- **Masonite** 5 + **Masonite ORM** 3
- **Tailwind CSS v4** + **Vite** (asset pipeline, not used by the auth templates yet)
- **SQLite** (dev / test) / **Postgres** (production target)
- **pytest** + **ruff**

## Local setup

```bash
# 1. Install dependencies
uv sync

# 2. Copy environment template
cp .env-example .env

# 3. Generate APP_KEY (Fernet, 44 chars)
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Paste the printed value into APP_KEY= in .env

# 4. Create the database and seed an owner account
rm -f database.sqlite3
python craft migrate
python craft seed:run

# 5. Run the dev server
python craft serve
# → http://localhost:8000

# 6. In a second terminal, watch the asset pipeline
npm install
npm run dev
```

## Seeded credentials (dev only)

After `craft seed:run`:

- **Workspace:** Acme Workspace (slug `acme`)
- **Owner email:** `owner@acme.test`
- **Owner password:** `password1234`
- **Verified:** yes (auto-verified when `MAIL_DRIVER=terminal`)

## Tests

```bash
pytest -q
```

The test suite covers real auth flows: signup creates a tenant + owner, login uses a real bcrypt hash, logout clears the session, password reset consumes a single token, email verification flips `verified_at`, and a tampered tenant id is rejected.

## Configuration

All config is environment-driven. See `.env-example` for the full list. The non-obvious defaults:

- `MAIL_DRIVER=terminal` — emails print to stdout. Switch to `smtp` in production and fill `MAIL_HOST` / `MAIL_PORT` / `MAIL_USERNAME` / `MAIL_PASSWORD`.
- `SESSION_DRIVER=cookie` — signed-cookie session, no server-side store.
- `DB_CONNECTION=sqlite` for dev, `postgres` for production (fill the `DB_*` block).

## Project structure

```
app/
  controllers/        HTTP request handlers
  mailables/          Transactional email classes
  middlewares/        Request lifecycle hooks (incl. TenantContextMiddleware)
  models/             ORM models (Tenant, User)
  providers/          App boot hooks
  utils/              Pure helpers (slugify, auth URL builders)
config/               All Masonite config modules
databases/
  migrations/         Schema changes (timestamped)
  seeds/              Dev / test data
routes/
  web.py              HTTP routes
templates/
  auth/               Login, register, password reset, verify email views
  emails/             Transactional email templates
  welcome.html        Tenant-aware landing page
tests/                pytest suite
```

## Out of scope (intentional)

Subdomain or path-based tenant routing, tenant switching UI, invitations, role / permission model beyond "owner", profile editing, password change from inside the app, 2FA, social login, billing, ERP modules (invoicing, inventory, customers, finance, reporting), API tokens, audit log, production SMTP hardening, i18n, SPA / HTMX. These are explicit non-goals for milestone 1.
