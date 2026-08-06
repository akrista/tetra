# Tetra

Multi-tenant SaaS ERP. **Milestone 1: authentication foundation. Milestone 2: dashboard, users, roles & permissions, profile.**

## Stack

- **Python** 3.12
- **Masonite** 5 + **Masonite ORM** 3
- **Tailwind CSS v4** + **Vite** (asset pipeline used by the auth, app, error, and maintenance templates)
- **SQLite** (dev / test) / **Postgres** (production target)
- **pytest** + **ruff**

## Local setup

```bash
# 1. Install dependencies
uv sync

# 2. Copy environment template
cp .env-example .env

# 3. Generate APP_KEY
python craft key

# 4. Create the database and seed an owner account
python craft migrate

# 5. Run the dev server
python craft serve

# 6. In a second terminal, watch the asset pipeline
bun install
bun run dev
```
## Tests

```bash
pytest -q
```

The test suite covers real auth flows: signup creates a tenant + owner, login uses a real bcrypt hash, logout clears the session, password reset consumes a single token, email verification flips `verified_at`, and a tampered tenant id is rejected. Milestone 2 adds coverage for the dashboard, profile (name/phone/password/email changes), tenant-scoped user CRUD, RBAC matrix (owner bypass, permission enforcement, escalation guards), cross-tenant IDOR, and role-preselection rendering.

## Configuration

All config is environment-driven. See `.env-example` for the full list. The non-obvious defaults:

- `MAIL_DRIVER=terminal` — emails print to stdout. Switch to `smtp` in production and fill `MAIL_HOST` / `MAIL_PORT` / `MAIL_USERNAME` / `MAIL_PASSWORD`.
- `SESSION_DRIVER=cookie` — signed-cookie session, no server-side store.
- `DB_CONNECTION=sqlite` for dev, `postgres` for production (fill the `DB_*` block).
- `COOKIE_SECURE=false` — set `true` when serving behind HTTPS so all cookies get the `Secure` flag.
- `AUTH_AUTO_VERIFY` — optional explicit override for auto-verifying new accounts. When unset, accounts auto-verify only under `MAIL_DRIVER=terminal` (dev convenience); with a real mail driver, email verification is enforced.

## Project structure

```
app/
  controllers/        HTTP request handlers
  mailables/          Transactional email classes
  middlewares/        Request lifecycle hooks (incl. TenantContextMiddleware)
  models/             ORM models (Tenant, User, Role, Permission)
  providers/          App boot hooks
  utils/              Pure helpers (slugify, auth URL builders)
config/               All Masonite config modules
databases/
  migrations/         Schema changes (timestamped)
  seeds/              Dev / test data (incl. permission catalog)
routes/
  web.py              HTTP routes
templates/
  auth/               Login, register, password reset, verify email views
  app/                Authenticated app shell (dashboard, users, roles, profile)
  emails/             Transactional email templates
  welcome.html        Tenant-aware landing page
  tests/                pytest suite
```

## Roadmap

Confirmed for v1:

- **ERP modules** — Productos, Ventas, Almacenes, Facturación (SENIAT-compliant), Clientes, Reportes, with multi-currency (VES/USD), IVA, IGTF, and retenciones.
- **Invitations** — token-based employee onboarding, replacing direct user creation.
- **Audit log** — fiscal-critical events only (invoice lifecycle, stock adjustments, exchange-rate changes), not a global logger.
- **Progressive enhancement (HTMX-style)** — interactive POS/sales flow on top of server-rendered pages. No SPA.
- **SMTP hardening** — production mail config (TLS, SPF/DKIM) and documented credentials handling.

Explicitly not in v1:

- Path-based tenant routing and tenant switching — v1 is one instance per business; tenant identification is an open decision deferred to Tetra Cloud.
- SaaS billing — self-hosted has no subscriptions; cloud tiers/pricing are undecided.
- A standalone finance module — the fiscal core (IVA/IGTF/retenciones) plus CxC aging covers SMB needs.
- API tokens — no integration consumer yet.
- An i18n framework — the product is es-VE by design; strings are hardcoded Spanish.
- 2FA — optional, owner-only TOTP; low priority, may be added later.
