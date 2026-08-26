---
name: Tetra
description: Tu negocio, en vivo — open-source ERP console para PyMEs venezolanas
colors:
  light-bg: "#f3f6f1"
  light-bg-soft: "#e9efe7"
  light-surface: "#ffffff"
  light-surface-2: "#eef3ec"
  light-text: "#16231b"
  light-text-soft: "#44584b"
  light-text-faint: "#5b6d63"
  light-primary: "#1d6e42"
  light-primary-strong: "#165634"
  light-primary-ink: "#ffffff"
  light-live: "#16a35a"
  light-amber: "#d99a13"
  light-amber-deep: "#8a5a0a"
  light-danger: "#b3261e"
  dark-bg: "#0b100d"
  dark-bg-soft: "#0e1511"
  dark-surface: "#121b15"
  dark-surface-2: "#17221b"
  dark-text: "#e7efe9"
  dark-text-soft: "#a9bdb1"
  dark-text-faint: "#788c80"
  dark-primary: "#3aa572"
  dark-primary-strong: "#4cc185"
  dark-primary-ink: "#0b140e"
  dark-live: "#34d98b"
  dark-amber: "#f0b95c"
  dark-amber-deep: "#e5a83f"
  dark-danger: "#f07067"
typography:
  display-body:
    fontFamily: "Sora, system-ui, -apple-system, Segoe UI, sans-serif"
    fontWeight: 400
    fontSize: "1rem"
    lineHeight: 1.5
  data:
    fontFamily: "IBM Plex Mono, JetBrains Mono, ui-monospace, monospace"
    fontWeight: 500
    fontSize: "0.78rem"
    fontFeature: "\"tnum\" 1, \"zero\" 1"
  scale:
    step-1: "0.6rem"
    step-2: "0.62rem"
    step-3: "0.64rem"
    step-4: "0.66rem"
    step-5: "0.68rem"
    step-6: "0.7rem"
    step-7: "0.72rem"
    step-8: "0.74rem"
    step-9: "0.75rem"
    step-10: "0.76rem"
    step-11: "0.78rem"
    step-12: "0.8rem"
    step-13: "0.82rem"
    step-14: "0.85rem"
    step-15: "0.9rem"
    step-16: "0.92rem"
    step-17: "0.95rem"
    step-18: "1rem"
    step-19: "1.05rem"
    step-20: "1.15rem"
    step-21: "1.2rem"
    step-22: "1.25rem"
    step-23: "1.35rem"
    step-24: "1.5rem"
    step-25: "1.6rem"
    step-26: "1.9rem"
    step-27: "2rem"
    step-28: "2.4rem"
    step-29: "2.6rem"
    step-30: "3.5rem"
    step-31: "4rem"
    step-32: "6rem"
    step-33: "7rem"
    step-34: "12rem"
rounded:
  card: "12px"
  card-lg: "16px"
  control: "8px"
  bar-top: "3px"
  pill: "999px"
spacing:
  page-x: "2.5rem"
  section-y: "4rem"
  container-max: "80rem"
  hairline: "1px"
components:
  cta-primary:
    backgroundColor: "{colors.light-primary}"
    textColor: "{colors.light-primary-ink}"
    typography: "{typography.display-body}"
    padding: "0.9rem 1.4rem"
  cta-ghost:
    backgroundColor: "{colors.light-surface}"
    textColor: "{colors.light-text}"
    typography: "{typography.display-body}"
    padding: "0.9rem 1.4rem"
  nav-pill:
    textColor: "{colors.light-text-soft}"
    typography: "{typography.display-body}"
    padding: "0.5rem 1rem"
---

# Design System: Tetra

## Overview

**Creative North Star: "La Consola Viva"**

Tetra's visual world is a real-time operations console for the Venezuelan PyME. Forest green is the healthy operational state — stock present, sale recorded, money counted. Corporate trust comes from a precise banking-grade data grid; the "most up to date tech" signal comes from live animated figures. Light theme is the paperwork day; dark theme is the operations floor. The page runs the owner's business live in front of her: "Tu negocio, en vivo."

The committed direction, lifted from the HTML comment in `templates/welcome.html`, is the binding thesis:

> **THESIS:** Tetra is the living console of the Venezuelan PyME — a real-time operations floor where green means the business is alive: stock present, sale recorded, money counted. Where legacy ERPs freeze on a 2008 screen, Tetra is live and legible.
> **OWN-WORLD:** Forest-green operations system. Light theme is the paperwork day; dark theme is the operations floor (system default, persisted toggle). Sora carries display and body in a single corporate-tech voice; IBM Plex Mono carries only fiscal and data figures. Soft offset shadows, 12–16px card radii, hairline data-grid separators. One authored moment: the hero metrics count up like a live console.
> **STORY:** A Venezuelan SMB owner lands, sees the console of her own business running live — sales counted, stock watched, fiscal numbers in order — reads "Tu negocio, en vivo", and clicks "Crear mi negocio" to make the console hers.
> **FIRST VIEWPORT:** Top bar (brand + theme toggle). Hero left: "Tu negocio, en vivo." with green emphasis, product subline, CTA "Crear mi negocio →" and ghost "Iniciar sesión", trust line. Hero right: the live operations console — metrics counting up, weekly activity bars, recent movements, live status dot "En operación", fiscal chips. Module strip below, footer.
> **FORM:** La Consola Viva. Position: candidate 6 of grounded list. Seed key: 13f9bd03.

**Key Characteristics:**
- **Theme is a first-class feature, not a skin.** The system ships both themes in CSS variables. Light = `:root`, dark = `:root[data-theme="dark"]`. An inline head script sets `data-theme` on `<html>` from `localStorage('tetra-theme')` before first paint, defaulting to `prefers-color-scheme`. The top-bar toggle flips it and persists. Every surface (landing, auth, app shell, errors) runs the same token system.
- **One typeface family, three weights; mono has one job.** Sora (400–800) carries every display, heading, and body string. IBM Plex Mono carries only fiscal and data figures (`"tnum" 1, "zero" 1` for tabular alignment). No Big Shoulders, no secondary display face — a single voice reads as modern corporate tech.
- **Green is the signal.** Forest `--primary` drives CTAs, links, the brand mark, active nav, summary values, success banners. `--live` (brighter green) drives the pulsing operational dot. Amber is reduced to a warning accent (low stock, IGTF/SENIAT notes); danger red is reserved for destructive actions and errors.
- **Elevation is soft, never hard.** 8/12/16px radii and soft offset+blur shadows. No 90° corners, no `4px 4px 0` slabs — a clean break from the previous mural world.
- **One authored moment.** The hero console metrics count up on load (easeOutExpo, es-VE formatting) plus a slow `livePulse` on the operational dot. Everything else is hover/focus transitions. `prefers-reduced-motion: reduce` kills all of it.
- **Spanish-first, es-VE.** All copy is Spanish. No translation artefacts.

Open product decisions that future design work must not silently close (from `PRODUCT.md` § Capabilities and Constraints): final OSS license (AGPL-3.0 working default); single-tenant vs multi-sucursal in v1; inventory costing method; direct SENIAT / fiscal-printer integration vs printable-document-only; offline / degraded-network mode depth; legacy ERP and Excel importer priority and depth; managed-cloud plan tiers and pricing; tenant identification strategy. New surfaces ship as the world, not as answers to these.

## Theme System

- **Defaults to the OS.** First visit: `matchMedia('(prefers-color-scheme: dark)')` decides. No flash of wrong theme: the inline script runs in `<head>` before the stylesheet loads.
- **Persists the manual choice.** The top-bar `.theme-toggle` flips `html[data-theme]` and writes `localStorage['tetra-theme']` to `dark` / `light`. A stored value always wins over the OS.
- **Toggle affordance.** The button always shows both sun and moon glyphs; CSS hides the moon in light and the sun in dark, so the label reads as "switch to the other theme." `aria-label="Cambiar tema"`.
- **Token pairs.** Every color exists in both themes under the same name (`--bg`, `--surface`, `--text`, `--primary`, …). Components reference tokens only — a new surface is themed for free.

## Colors

The palette is a forest in two states: paperwork day (light) and operations floor (dark). Green is health; amber is a warning; red is an error. Every color has a job; none are decorative.

### Light theme (`:root`)
- **Forest Primary** (`#1d6e42`): the brand green. CTAs, links, brand mark, active nav, summary values, success banners. `--primary-strong` (`#165634`) is the pressed/hover shade; `--primary-ink` (`#ffffff`) is text on primary; `--primary-soft` (`rgba(29,110,66,.10)`) is green-tinted fills (active nav pill, focus contexts).
- **Live** (`#16a35a`): brighter operational green. The pulsing dot and "En operación" status. `--live-ring` (`rgba(22,163,90,.45)`) is the pulse ring.
- **Amber** (`#d99a13`): warning accent. Low-stock trends, IGTF/SENIAT notes, owner-badge. `--amber-deep` (`#8a5a0a`) is amber text on light; `--amber-soft` (`rgba(217,154,19,.12)`) is amber fills.
- **Danger** (`#b3261e`): destructive actions and errors. `--danger-soft` (`rgba(179,38,30,.10)`) is error fills.
- **Neutrals:** `--bg` `#f3f6f1` (paperwork day), `--bg-soft` `#e9efe7` (showcase panels), `--surface` `#ffffff` (cards), `--surface-2` `#eef3ec` (table hover / inset), `--text` `#16231b`, `--text-soft` `#44584b` (secondary), `--text-faint` `#5b6d63` (tertiary, mono labels — ≥4.5:1 on light). `--border` `rgba(23,51,35,.12)` (hairlines), `--border-strong` `rgba(23,51,35,.26)`.

### Dark theme (`:root[data-theme="dark"]`)
- **Forest Primary** (`#3aa572`): brightened for dark. `--primary-strong` (`#4cc185`), `--primary-ink` (`#0b140e`) — dark text on the lighter green button, `--primary-soft` (`rgba(58,165,114,.16)`).
- **Live** (`#34d98b`), `--live-ring` (`rgba(52,217,139,.45)`).
- **Amber** (`#f0b95c`) / `--amber-deep` (`#e5a83f`) / `--amber-soft` (`rgba(240,185,92,.14)`).
- **Danger** (`#f07067`) / `--danger-soft` (`rgba(240,112,103,.14)`).
- **Neutrals:** `--bg` `#0b100d` (operations floor), `--bg-soft` `#0e1511`, `--surface` `#121b15`, `--surface-2` `#17221b`, `--surface-hover` `#1a271e`, `--text` `#e7efe9`, `--text-soft` `#a9bdb1`, `--text-faint` `#788c80`. `--border` `rgba(196,224,206,.13)`, `--border-strong` `rgba(196,224,206,.24)`.

### Rules
**The Green-Is-Health Rule.** Green means the business is operating: primary for action, live for live status, primary-soft for fills. It is the palette's signal color, used generously but never as background wallpaper.
**The Amber-Is-Warning Rule.** Amber marks attention: low stock, pending fiscal notes, unverified owners. It never competes with green for action.
**The Contrast Floor.** Body text and any label ≥4.5:1 against its background in both themes. `--text-faint` exists only where it clears the floor (measured 5.05:1 light, 5.36:1 dark).

## Typography

**Display + Body Font:** Sora (system-ui, -apple-system, Segoe UI, sans-serif) — geometric, modern, corporate-tech.
**Data Font:** IBM Plex Mono (JetBrains Mono, ui-monospace, monospace) — fiscal and data figures only, with `font-feature-settings: "tnum" 1, "zero" 1`.

**Character:** One family, one voice. Sora 800 with tight tracking carries display; Sora 400 explains. IBM Plex Mono counts. The system is deliberately single-voice — a second display face would read as decorative, not operational.

### Type Ramp (light = dark, tokens not needed — type is theme-independent)
- **Hero Title** (Sora 800, `clamp(2.6rem, 5.2vw, 4rem)`, line-height 1.05, letter-spacing -0.03em): the landing h1.
- **Page Title** (Sora 800, `clamp(1.9rem, 3.5vw, 2.6rem)`, letter-spacing -0.02em): dashboard/app page heads.
- **Auth Title** (Sora 800, 1.9rem): auth-card headings.
- **Section / Card Title** (Sora 600–700, 1–1.15rem): panel and card headings.
- **Body** (Sora 400, 0.98–1rem, line-height 1.6): sublines, descriptions, form text. Hero sub capped at `max-width: 30rem`.
- **Meta / Small** (Sora 400–500, 0.78–0.85rem): secondary text, trust line, table cells.
- **Data / Fiscal (mono)** (IBM Plex Mono 400–600, 0.6–1rem): every metric value, monetary figure, SKU, date, table numeric, version string. Never used for prose. The metric value is mono 1.6rem weight 600; the summary value is mono 2rem weight 600.

### Named Rules
**The Data-Mono Rule.** Mono is fiscal data, not costume. If a string has no number, date, or label attached to a number, it is Sora. The metric tiles, tables, totals, and fiscal chips are mono; paragraphs and headings never are.
**The No-Kicker Rule.** No kicker, eyebrow, or section number above a heading. The green accent span inside a heading (`.accent`) is the only emphasis device.

## Layout

The container is centered at `max-width: 80rem` with `2.5rem` side padding at desktop, `1.5rem` at tablet, `1.25rem` at phone. The landing hero is a two-column grid (`minmax(0,1fr)` / `minmax(20rem,26rem)`) with a `3rem` gap, collapsing to one column at `max-width: 960px`. The auth shell is `1fr` / `30rem` at desktop, one column below `1024px`. The app content is `max-width: 64rem`.

Vertical rhythm: top bar (`1.25rem` padding, `1px` border-bottom), hero (`4rem` top / `2.5rem` bottom), billing strip (`1.5rem` padding bracketed by `1px` hairlines), footer (`2rem` top / `2.5rem` bottom).

## Elevation & Depth

Depth is soft, from the tokenized shadow ramp:
- `--shadow-sm`: `0 1px 2px rgba(16,32,24,.06)` — cards, inputs.
- `--shadow-md`: `0 4px 12px rgba(16,32,24,.08)` — auth card, popovers.
- `--shadow-lg`: `0 12px 32px rgba(16,32,24,.12)` — the hero console card.

**The Soft-Elevation Rule.** Depth is a soft offset+blur shadow, never a hard colored slab, never a 1px border under a heavy shadow. The console card carries `--shadow-lg` and no border; a quiet surface carries `--shadow-sm` plus a `--border` hairline.

## Shapes

Radii come from three tokens: `--radius-sm: 8px` (buttons, inputs, badges), `--radius: 12px` (cards, panels, nav pills are a 999px exception), `--radius-lg: 16px` (the hero console card, auth card emphasis). Focus is a green ring: `--focus-ring: 0 0 0 3px rgba(...)` in the theme's primary.

**The Rounded-Control Rule.** Controls and cards are gently rounded; pills are reserved for navigation/status chips. Nothing is sharp-cornered.

## Components

### Buttons
- **Primary (`.cta`, `.btn`):** forest primary background, `--primary-ink` text, `--radius-sm`. Hover: `--primary-strong`. The trailing arrow (`.cta-arrow`) is mono and slides 4px right on hover.
- **Ghost (`.cta-ghost`, `.btn-ghost`):** `--surface` background, `--border`, `--text`. Hover: surface-hover + border-strong.
- **Danger (`.btn-stamp`):** transparent, danger border+text. Hover: danger background, white text. Destructive actions only.
- **Focus-visible:** `--focus-ring` (green) on every control.
- **Motion:** transitions 0.15–0.2s ease. Reduced-motion disables them.

### Nav Pills (`.nav-pill`, `.app-nav-link`)
- **Shape:** 999px pill, `--radius-sm` padding `0.5rem 1rem`, Sora 0.85rem, `--text-soft`.
- **Active (`.is-active`):** `--primary-soft` background, `--primary` text. In the app shell, the active link is the current module.

### Top Bar (`.topbar`)
- **Layout:** flex, `justify-content: space-between`, padding `1.25rem 2.5rem` (`1.5rem` ≤960px), `1px` `--border` bottom hairline, `--topbar-bg` (surface).
- **Brand (`.brand`):** 1.9rem custom SVG mark — a `40×40` green tile (`rx="10"`) with a cream "T" cut inside — plus the "Tetra" wordmark (Sora 700, 1.15rem).
- **Theme toggle (`.theme-toggle`):** 2.5rem circle, border, hover surface-hover. Shows the sun in light, the moon in dark.
- **Meta (`.topbar-meta`):** app-shell tenant name, mono, `--text-faint`. Hidden ≤960px.

### Landing Hero (`.hero`)
- **Left column:** h1 "Tu negocio, **en vivo**." with the `.accent` span in forest primary; `.hero-sub` product subline; `.hero-cta` (primary "Crear mi negocio →" + ghost "Iniciar sesión"); `.hero-trust` line ("Open source · Self-hosted · Tus datos, tu servidor").
- **Right column (`.hero-figure`):** the live console demo (`.console-card`).

### The Console Card (`.console-card`) — the hero proof
- **Shell:** `--surface`, `--radius-lg`, `--shadow-lg`, no border. A `::before` radial `--primary-soft` glow sits behind the hero grid (subtle, non-decorative depth).
- **Head (`.console-head`):** title "Panel de operaciones" (Sora 600) + `.live-pill` ("En operación") — `--primary-soft` pill with a `.live-dot.pulse` green dot.
- **Metrics (`.console-metrics`):** 2-column grid, `gap: 1px`, `background: var(--border)` producing hairline dividers between cells. Each `.metric` has `.metric-label` (mono, `--text-faint`, uppercase) and `.metric-value` (mono 1.6rem 600) with a `.metric-trend` (`.up` in primary, `.warn` in amber).
- **Bars (`.console-bars`):** 7 mono day labels (L M M J V S D) over a 7-column bar row; `.bar.hi` marks the peak day in primary, the rest `--primary-soft`.
- **Activity (`.console-activity`):** recent-movement list — name + amount, `--border` hairlines, `.act-dot.ok` green ticks.
- **Foot (`.console-foot`):** `.fiscal-chip` amber pills (IVA / IGTF 3% / SENIAT) + `.console-sample` "Datos de muestra".
- **Semantics:** the whole card is `role="img"` with an `aria-label` describing the demo; the count-up lives on `data-count-to` / `data-count-decimals` / `data-count-prefix` attributes driven by `app.js`.

### Billing Strip (`.billing`)
- Full-bleed band bracketed by `1px` hairlines; `.billing-item` pills with a `.billing-dot`. `.accent` items are green (Productos, Ventas, Almacenes, Facturación fiscal, Clientes, Reportes); `.warn` items amber (IGTF, SENIAT); default items neutral (Multi-moneda, Self-hosted, Código abierto).

### Footer (`.foot`)
- Flex, space-between, mono 0.7rem uppercase `--text-faint`. Left: "Tetra · La consola de tu negocio, en vivo". Right: "v0.1 · Hecho en Venezuela".

### Auth Shell (`.auth-shell`)
- **Showcase (`.auth-showcase`, desktop ≥1024px):** `--bg-soft` panel with the brand, the declaration "Tu negocio, en vivo. La consola de tus operaciones." with `.accent`, and a `.auth-features` list (Inventario y ventas en tiempo real / Facturación fiscal SENIAT / SENIAT · IVA · IGTF / VES + USD) — each item prefixed by a green live dot.
- **Form pane (`.auth-form-pane`):** the `.auth-card` on `--surface`, `--radius-lg`, `--shadow-md`. `.auth-mobile-brand` replaces the showcase on ≤960px.
- **Form controls:** `.form-label` (mono uppercase, `--text-faint`), `.form-input` (`--radius-sm`, `--border`; focus = primary border + `--focus-ring`; `[aria-invalid]` = danger border), `.password-wrap` + `.password-toggle`, `.form-check` with `accent-color: var(--primary)`, `.error-message` (danger), `.alert-banner` (green default; `[role="alert"]` becomes red), `.auth-icon` (4.5rem green tile for verify_email).

### App Shell (`.app-content`)
- **Page head (`.page-head`):** `.page-title` + `.page-sub` + `.page-actions` (primary + ghost buttons). Column-stacks ≤960px.
- **Panels (`.panel`):** `--surface`, `--radius-lg`, `--shadow-sm`, `.panel-title`.
- **Tables (`.data-table`):** mono cells, `--text-faint` uppercase headers, row hover `--surface-2`, wrapped in `.data-scroll`. `.table-action` (primary), `-danger`, `-disabled`.
- **Summary (`.summary-grid`):** auto-fit cards; `.summary-card` hover raises a primary border; `.summary-value` mono 2rem primary.
- **Badges:** `.role-badge` (green), `.owner-badge` (amber).
- **States:** `.empty-state`, `.form-actions` + `.form-notes`, `.confirm-inline` (danger inline confirm).

### Error Pages (`.standalone`)
- **Art:** the existing warm-sunset SVG illustrations (`storage/static/svg/{403,404,500,503}.svg`) sit on a `--primary-soft` slab (`.standalone-art-slab`) with an 0.85rem translate — the slab frames the old art in the new green world.
- **Code (`.error-code`):** Sora 800, `clamp(6rem,22vw,12rem)`, letter-spacing -0.04em. `.error-bar` is a short primary pill; `.error-msg` explains; `.standalone-actions` offers the CTA.
- **Brand (`.standalone-brand`):** the green-tile mark, linked to `/`.

### Emails (`.emails/layout.html`)
- Inline-styled, theme-independent (email clients ignore the app theme). Dark `#0b100d` outer, `#f3f6f1` card, Sora 800 headings in `#16231b` (system font stack, no CDN), `.btn` `#1d6e42` background, `.url` `#1d6e42`, `.muted` `rgba(22,35,27,.62)`, `.footer` `rgba(243,246,241,.6)`.
- **Email type ramp:** the sizes are intentionally compressed (14–18px) for client compatibility — this is the sanctioned exception to the web ramp.

## Motion

- **One authored moment:** the hero console metrics count up on load — rAF-driven, 1400ms, `easeOutExpo`, es-VE number formatting (`toLocaleString('es-VE')`). Driven from `data-count-to` attributes in `app.js`.
- **Ambient life:** the `.live-dot.pulse` ring (`@keyframes livePulse`, slow opacity ring) says the console is running.
- **Micro-interaction:** theme-toggle color cross-fade (0.2s), button/arrow hovers, link hovers. All transitions ≤0.2s.
- **Reduced motion:** a global `@media (prefers-reduced-motion: reduce)` sets every transition/animation to near-instant, and `app.js` checks the same flag to set count-up final values instantly without animating.

## Do's and Don'ts

### Do
- **Do** ship new surfaces in the shared token system — components reference `var(--*)` only, so both themes stay free.
- **Do** use Sora for all display/body and IBM Plex Mono for data and fiscal figures only, with tabular numerals.
- **Do** keep green as the action/live signal and amber as the warning. Never swap their jobs.
- **Do** use soft shadows and 8/12/16px radii. No hard offset slabs.
- **Do** write copy in es-VE first; translate never.
- **Do** respect `prefers-reduced-motion` — a new animation needs a world reason, and it must have a reduced-motion path.

### Don't
- **Don't** introduce a second display typeface or decorative mono. One family + data mono is the system.
- **Don't** add glass, blur, or `backdrop-filter` as decoration. The world is matte and legible.
- **Don't** use Tailwind utility chains in component CSS — write the world in semantic class names (`.cta`, `.console-card`, `.panel`). Tailwind v4 is loaded for the `@source` path only.
- **Don't** place hard offset shadows, 90° corners, or the old mural tokens (`--paper`, `--ink`, `--stamp`, Big Shoulders) in new work.
- **Don't** ship a light-only or dark-only surface; every new page runs both themes.
- **Don't** close the open product decisions from `PRODUCT.md` by inventing UI for them (fiscal tiers, sucursales, costing, cloud pricing).

## Implementation Status

The world is built across landing, auth, and the app shell, served from the existing Masonite routes.

| Ingredient | Status |
|---|---|
| Theme system (inline init + toggle + localStorage) | Present — all layouts |
| Sora + IBM Plex Mono Bunny CDN | Present |
| `.brand-mark` green tile SVG | Present — landing, auth, app, errors |
| `.topbar` + `.theme-toggle` | Present — landing, auth, app |
| Landing hero + `.console-card` live demo (count-up, bars, activity, fiscal chips) | Present — `welcome.html` |
| Count-up motion + livePulse + reduced-motion kill | Present — `app.js` |
| `.billing` module strip + `.foot` | Present |
| Auth shell (showcase + form pane + mobile brand) | Present — `auth/layout.html` |
| App shell (page head, panels, data tables, summary, badges) | Present — `app/layout.html` + module templates |
| Error pages (`standalone`, green slab framing kept sunset SVGs) | Present |
| Maintenance page | Present (no route — template only) |
| Email layout (forest re-tone, Sora, inline-safe ramp) | Present |
| Tailwind v4 `@source "../../templates"` | Present — `resources/css/app.css` |
| `/register` and `/login` destination pages | **Stub** — routes exist; per `PRODUCT.md` handlers redirect without rendering views (auth views are pre-built in `templates/auth/`) |
| `/logout` form | **Stub** — route exists, behavior placeholder |
| Dashboard / module data (live queries behind the console demo) | **Deferred** — hero uses labeled sample data; wiring real aggregates is future work |
| Fiscal pricing tiers, plan badges, comparison tables | **Deferred** — out of scope until managed-cloud pricing is decided |
| Reserved tokens, secondary surfaces | **Deferred** — the token system is the extension point |
