# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Owners and operators of small and medium-sized businesses in Venezuela. The typical user is the dueño or administradora of a tienda, ferretería, distribuidora, comercializadora, or small manufacturer who runs sales, inventory, and billing on the same machine or VPS they use for everything else. They are non-technical, expect a fast modern web app, work primarily in a desktop browser, and frequently check on their phone between sales. They have been forced to use legacy Venezuelan ERPs that are slow, ugly, charge per-seat, lose data, and still print on dot-matrix paper — they switch when a tool is visibly modern, faster, and not a hostage situation.

Other audiences (confirmed by use, not by request):
- Employees of the same SMB (cashier, warehouse clerk) who need a constrained role inside the same business.

## Product Purpose

Tetra is an open-source ERP web application built for Venezuelan small and medium-sized businesses. Each business runs its own instance — self-hosted on a VPS or on-prem, or eventually on a managed cloud — and uses Tetra to manage products, sales, warehouses, and customer invoicing, the daily operational spine of a Venezuelan SMB, in Spanish, with the fiscal rules Venezuelan tax law actually requires.

Success for v1 = a Venezuelan SMB can install Tetra, register their business, configure their RIF and fiscal data, manage products and stock across one or more warehouses, register sales, issue SENIAT-compliant customer invoices (facturas) in VES and USD with IVA and IGTF handled correctly, and pull a clean report at month-end without exporting to Excel.

## Positioning

Tetra is the open-source, self-hosted, modern alternative to the legacy Venezuelan ERP market — the closed, ugly, slow, per-seat tools that dominate tiendas, ferreterías, and distribuidoras. The differentiator is not feature breadth: it is that a Venezuelan SMB owns their data, owns their instance, and uses a tool that does not look and feel like it was shipped in 2008. Tetra must visibly and operationally outclass the legacy incumbents — speed, visual quality, Spanish-native copy, fiscal correctness — without copying the enterprise-ERP playbook of bloated menus and consultant-driven deployments.

Open source is load-bearing: it is how the product earns community trust and avoids the hostage dynamics of per-seat licenses and locked databases.

## Operating Context

- Primary device: modern desktop or laptop browser. Secondary: mobile phone (responsive web; no native app in v1) for quick lookups — checking a stock number, marking a sale paid, viewing a day's invoices.
- Primary language: Spanish (es-VE). All user-facing copy, labels, error messages, and printable documents are in Spanish. English is acceptable in code, logs, and developer tooling.
- Primary currencies: Bolívar (VES) and US Dollar (USD). The system records both, supports transactions in either, and reports per currency and consolidated. Exchange rates are user-managed per business day.
- Fiscal context: every customer invoice is a Venezuelan factura legal. It carries sequential numbering, the customer's RIF or CI, IVA breakdown, the relevant retenciones, and is printable on plain paper or a fiscal printer.
- Each business is one tenant. The system is single-tenant per instance: a self-hosted install serves one business; the future managed cloud serves many isolated tenants behind one deployment. Tenant isolation must hold in both modes.
- Connectivity is unreliable in parts of Venezuela; the system is online-first but must not block common operations on a degraded local network.
- The user already runs the business on a mix of papel, Excel, and the legacy ERP. Migration is a real job — onboarding and import are part of the product experience, not a future nice-to-have.

## Capabilities and Constraints

Confirmed for v1:

**Deployment and licensing**
- Open source. Working default license is AGPL-3.0; final choice belongs to the project owner and is recorded here once decided.
- Self-hosted is the primary mode. One Docker-deployable instance per business.
- A managed cloud option (Tetra Cloud) is part of the product roadmap; it ships after v1 self-hosted is stable.
- Source-available; no telemetry that phones home without the operator's explicit opt-in.

**Modules in v1**
- **Productos (Products):** catalog with SKU, name, description, cost, price(s), units, IVA rate, category, and per-warehouse stock.
- **Ventas (Sales):** sales orders and POS-style sales; line items, taxes, discounts, payment recording.
- **Almacenes (Warehouses):** multi-warehouse stock, transfers between warehouses, stock adjustments, low-stock alerts.
- **Facturación (Customer Invoicing / CxC):** SENIAT-compliant customer invoices (factura, nota de crédito, nota de débito), sequential numbering per fiscal series, customer RIF/CI, IVA breakdown, accounts-receivable tracking.
- **Clientes (Customers):** customer records with RIF, CI, address, contact, credit terms, and balance.
- **Reportes (Reports):** sales by period, top products, low stock, accounts-receivable aging, sales by currency.

**Venezuelan fiscal and monetary correctness (v1 must-haves)**
- Multi-currency: every monetary record carries a currency (VES or USD) and the exchange rate for the transaction date. Base currency is configurable per business.
- IVA: configurable rate(s), breakdown on every invoice line, totals and retenciones on the printed document.
- IGTF: 3% deduction on payments in foreign currency, applied automatically where the law requires it and configurable where it does not.
- Retenciones: IVA retenido and ISLR retenido when applicable, recorded on the invoice and reflected in reports.
- Sequential invoice numbering per fiscal series, no gaps, no reuse, recoverable on reprint.
- Printable factura legal layout (plain paper and fiscal-printer-friendly).

**Technical**
- Web app, responsive, no native mobile client in v1.
- Stack already committed: Masonite 5 + Masonite ORM 3, Python 3.14, Tailwind v4 via Vite.
- Local dev: SQLite. Production: Postgres.
- Backups are the operator's responsibility per instance, with documented procedures.

Explicitly open / not yet decided:
- Final open source license (AGPL-3.0 working default; may change).
- Subdomain vs path vs header for tenant identification in the future managed cloud.
- Role / permission model beyond owner and basic staff roles.
- Whether v1 supports a single business with multiple sucursales (branches) under one tenant.
- Inventory costing method (FIFO / LIFO / weighted average) and re-valuation handling.
- Direct SENIAT / fiscal-printer integration vs printable-document-only output.
- Offline / degraded-network mode depth.
- Importers from legacy Venezuelan ERPs and from Excel — priority and depth.
- Plan tiers and pricing for the future managed cloud.

## Brand Commitments

- Product name: **tetra**.
- Open source, community-trust identity. Not enterprise, not consulting-led.
- Spanish (es-VE) is the language of the product's voice and UI.
- Visual identity must be modern, fast, and visibly outclass the legacy Venezuelan ERPs the target user is migrating from. This is a binding direction: the design reads as the new generation of SMB tooling, not as another clone of the legacy incumbents. Specific palette, typography, and visual recipes are decided in a later design pass, not here.
- Negative space: the design must not look like the legacy Venezuelan ERPs — no skeuomorphic invoice forms, no dot-matrix-era status bars, no 2008-era enterprise-ERP navigation patterns, no clinical blue/grey palettes that read as "business software circa 2005." What replaces these is a later design decision.

## Evidence on Hand

- Masonite 5 starter scaffold in this repo (Python 3.14, Masonite Framework 5, Masonite ORM 3, Tailwind v4 via Vite).
- `app/models/User.py` already wires `Authenticates`, `Authorizes`, and `Notifiable` traits and lists `name, email, password, phone` as fillable.
- `app/controllers/AuthController.py` provides route handlers for login, register, forgot/reset password, verify email, and logout. The current handlers are stubs that redirect without actually authenticating; they are a starting point, not a finished feature.
- `routes/web.py` exposes the auth routes.
- `config/auth.py` configures a `web` guard backed by the `User` model.
- `config/database.py` supports SQLite, MySQL, and Postgres.
- `tests/test_auth.py` exists as a placeholder for auth tests.

No ERP modules, no fiscal-invoicing engine, no multi-currency logic, no IGTF handling, no SENIAT integration, no real auth views, and no live SMTP integration exist yet. Future work must not invent customers, testimonials, or production metrics for the Venezuelan market.

## Product Principles

- **Venezuelan SMB first.** Every decision is filtered through: does this help a tienda, ferretería, or distribuidora in Venezuela do their job today? If it only helps a multinational rollout, it does not ship.
- **Fiscal correctness is non-negotiable.** A factura that is wrong by one cent on IVA, or that misses an IGTF deduction, is a liability for the business. The system either computes correctly or it does not ship that feature.
- **Own your data, own your instance.** Self-hosted is the primary mode. No telemetry, no phoning home, no lock-in. The business owns the database, the backups, and the migration path.
- **Modern is the moat.** The legacy incumbents win on inertia, not on quality. Tetra wins on visible quality: speed, visual design, copy that respects the user, and a workflow that does not feel like punishment.
- **Spanish-native, not Spanish-translated.** Labels, error messages, and documents read as if written in Spanish first. The legacy tools read as English-to-Spanish translation; Tetra does not.

## Accessibility & Inclusion

No formal WCAG target has been confirmed yet, but: the user base works in Spanish on shared hardware in mixed lighting, and the design must remain readable on small phones and accessible across a wide range of literacy and tech comfort. Common semantic HTML and form best practices are the floor; a formal accessibility standard is set when the first non-auth surface ships.
