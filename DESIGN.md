---
name: Tetra
description: La factura que se diseña — open-source ERP mural para PyMEs venezolanas
colors:
  ink: "#0e0e10"
  ink-soft: "#1a1a1e"
  ink-deep: "#060607"
  paper: "#f1ead6"
  paper-soft: "rgba(241, 234, 214, 0.78)"
  paper-faint: "rgba(241, 234, 214, 0.42)"
  paper-line: "rgba(241, 234, 214, 0.18)"
  paper-line-soft: "rgba(241, 234, 214, 0.10)"
  amber: "#e0a020"
  amber-deep: "#b87a10"
  amber-glow: "rgba(224, 160, 32, 0.38)"
  amber-shadow: "rgba(224, 160, 32, 0.22)"
  stamp: "#c2362f"
  stamp-deep: "#8a1c1c"
typography:
  display:
    fontFamily: "Big Shoulders Display, Bebas Neue, Oswald, sans-serif"
    fontWeight: 900
    fontSize: "clamp(4.5rem, 12vw, 11rem)"
    lineHeight: 0.82
    letterSpacing: "-0.035em"
  body:
    fontFamily: "Sora, system-ui, -apple-system, Segoe UI, sans-serif"
    fontWeight: 400
    fontSize: "1rem"
    lineHeight: 1.5
  mono:
    fontFamily: "IBM Plex Mono, JetBrains Mono, ui-monospace, monospace"
    fontWeight: 500
    fontSize: "0.72rem"
    lineHeight: 1.5
    letterSpacing: "0.1em"
    fontFeature: "\"tnum\" 1, \"zero\" 1"
rounded:
  stamp: "50%"
spacing:
  page-x: "2.5rem"
  page-y: "1.5rem"
  section-y: "4rem"
  container-max: "96rem"
  hairline: "1.5px"
components:
  cta-primary:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.mono}"
    padding: "0.95rem 1.5rem"
  cta-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.paper}"
    typography: "{typography.mono}"
    padding: "0.95rem 1.5rem"
  nav-pill:
    textColor: "{colors.paper-soft}"
    typography: "{typography.mono}"
    padding: "0.5rem 1rem"
  fiscal-stamp:
    textColor: "{colors.stamp}"
    typography: "{typography.display}"
    size: "4.6rem"
---

# Design System: Tetra

## Overview

**Creative North Star: "El Mural de la Factura"**

Tetra's visual world is a public mural on a Venezuelan wall. The night wall is deep ink; the factura is painted on top in warm cream with a hard sour-amber shadow behind it; the legacy ERP's dot-matrix residue fades into the background as you scroll. The page declares itself — "La factura que se diseña. No la que se sufre." — and invites the SMB owner to "pintar" their own business. The brand voice is a muralist, not a SaaS template.

The committed direction, lifted from the HTML comment in `templates/welcome.html`, is the binding thesis:

> **THESIS:** Tetra is the public mural on the Venezuelan wall — the factura painted boldly where the legacy ERP's dot-matrix ghost used to be.
> **OWN-WORLD:** Night wall (deep ink) with warm cream paint, sour amber signal (30–60% of surface), fiscal red stamp. Condensed display (Big Shoulders Display) carries the declaration, mono (IBM Plex Mono) carries fiscal data, geometric sans (Sora) carries body.
> **STORY:** A Venezuelan SMB owner lands, sees the factura designed the way it should be, reads "La factura que se diseña. No la que se sufre.", and clicks "Crear mi negocio" to start.
> **FIRST VIEWPORT:** Top bar (brand + meta + nav). Hero left: TETRA in massive condensed caps, subline, declaration with amber emphasis on "se diseña" and strike-through on "se sufre", CTA "Crear mi negocio →" and ghost "Iniciar sesión". Hero right: the painted factura with hard amber shadow, legacy dot-matrix ghost fading behind. Billing block of product truth. Footer "Pintado para PyMEs venezolanas".
> **FORM:** Venezuelan street poster / mural. Position: candidate 7 of grounded list. Seed key: f8fdee6d.

**Key Characteristics:**
- **Sharp by default.** The only rounded element in the system is the FISCAL stamp (a circle). Everything else is 90° corners, ink hairlines, no card radii.
- **Three typefaces, three jobs.** Condensed display (Big Shoulders Display) declares; mono (IBM Plex Mono) carries fiscal data and metadata; geometric sans (Sora) carries body. No overlap.
- **Amber is the signal, not the chrome.** Sour amber (`#e0a020`) carries the CTA, the declaration emphasis, the brand-mark half, and the factura's hard offset shadow. It is the painter's color, not a brand tint.
- **Fiscal red is a stamp, not a palette.** A single circular FISCAL stamp, rotated -14°, sitting on top of the factura. Never used elsewhere.
- **One authored moment.** The legacy dot-matrix ghost fades as the user scrolls past the first viewport. Nothing else animates.
- **Spanish-first, es-VE.** All copy is Spanish. No translation artefacts.

Open product decisions that future design work must not silently close (from `PRODUCT.md` § Capabilities and Constraints, lines 70–79): final OSS license (AGPL-3.0 working default); role/permission model beyond owner and basic staff; single-tenant vs multi-sucursal in v1; inventory costing method (FIFO / LIFO / weighted average); direct SENIAT / fiscal-printer integration vs printable-document-only; offline / degraded-network mode depth; legacy ERP and Excel importer priority and depth; managed-cloud plan tiers and pricing; subdomain vs path vs header for tenant identification in the future managed cloud. New surfaces ship as the world, not as answers to these.

## Colors

The palette is a mural in three layers: the night wall underneath, the painted factura on top, and the amber/red signal that says "this is the new one." Every color has a job and a role in the layering; none are decorative.

### Primary
- **Sour Amber** (`#e0a020`): the painter's color. The CTA background, the brand mark's right half, the declaration emphasis, the hard offset shadow under the factura, the billing amber dots. Sits at 30–60% of the visible surface by design.
- **Amber Deep** (`#b87a10`): amber-against-paper. The totals-row total value (amber printed on the cream paper factura).
- **Amber Glow** (`rgba(224, 160, 32, 0.38)`): reserved for soft amber halos on future surfaces. Defined, no consumer in v1.
- **Amber Shadow** (`rgba(224, 160, 32, 0.22)`): reserved for low-opacity amber underlays on future surfaces. Defined, no consumer in v1.

### Tertiary
- **Fiscal Red** (`#c2362f`): the stamp. Used only for the circular FISCAL stamp on the factura and the strike-through on "se sufre." Its rarity is the point: red never decorates anything else.
- **Stamp Deep** (`#8a1c1c`): reserved for red-on-paper contexts on future surfaces. Defined, no consumer in v1.

### Neutral
- **Deep Ink** (`#0e0e10`): the wall. Page background, factura border and body text, the hover state for the primary CTA. The night the mural sits on.
- **Ink Soft** (`#1a1a1e`): reserved for layered surfaces over the wall (cards, modals). Defined, no consumer in v1.
- **Ink Deep** (`#060607`): reserved for the deepest voids (e.g. modal scrims). Defined, no consumer in v1.
- **Warm Cream Paper** (`#f1ead6`): the paint. The factura background, the primary text color on the wall, the TETRA wordmark, the declaration body, the hover swap state for the ghost CTA.
- **Paper Soft** (`rgba(241, 234, 214, 0.78)`): secondary text on the wall. Top-bar meta strong, hero sub, nav pill, billing, footer.
- **Paper Faint** (`rgba(241, 234, 214, 0.42)`): tertiary text on the wall. Top-bar meta values, declaration strike text, footer.
- **Paper Line** (`rgba(241, 234, 214, 0.18)`): hairlines on the wall. Nav pill border, ghost CTA border, footer separator.
- **Paper Line Soft** (`rgba(241, 234, 214, 0.10)`): the faintest hairlines. Top-bar border-bottom.

**The Amber Surface Rule.** Sour amber is the only color allowed to cover significant wall area (30–60% of any surface). Cream paint and ink text are the defaults; amber is the highlight that proves the highlight exists. If amber appears on every section, it is no longer a signal.

**The Stamp Singularity Rule.** Fiscal red (`#c2362f`) appears only inside the FISCAL stamp. It is not a palette accent; it is the stamp. A red line, red button, red badge, or red border anywhere else breaks the world.

## Typography

**Display Font:** Big Shoulders Display (Bebas Neue, Oswald, sans-serif) — condensed, poster.
**Body Font:** Sora (system-ui, -apple-system, Segoe UI, sans-serif) — geometric sans.
**Label/Mono Font:** IBM Plex Mono (JetBrains Mono, ui-monospace, monospace) — fiscal data and labels.

**Character:** Three faces, three jobs, no overlap. Big Shoulders Display shouts the declaration. IBM Plex Mono counts, labels, and dates with tabular numbers and a slashed zero. Sora explains. The hierarchy is enforced by role, not by weight alone.

### Hierarchy
- **Hero Title** (weight 900, `clamp(4.5rem, 12vw, 11rem)`, line-height 0.82, letter-spacing -0.035em, uppercase): the TETRA wordmark in the hero. The single loudest voice on the page. Collapses to `clamp(3.5rem, 16vw, 6rem)` on tablets and `clamp(2.8rem, 14vw, 4.5rem)` on phones. The display scale runs past the 6rem floor deliberately — the world is poster-scale, the wall is the room.
- **Declaration** (weight 800, `clamp(1.5rem, 2.6vw, 2.4rem)`, line-height 1.05, uppercase): the "se diseña / se sufre" line under a 2px amber top-border.
- **Display Inline** (weight 800, 1.4–1.7rem, line-height 1, uppercase): brand wordmark (1.4rem), factura "Factura" doc-type (1.7rem), FISCAL stamp text (0.75rem).
- **Body** (weight 400, 1rem, line-height 1.5): explanations — the hero sub, 0.98rem at desktop / 0.92rem on phones, max-width 30rem (≈ 65ch).
- **Mono Label** (weight 500–600, 0.6–0.85rem, uppercase, letter-spacing 0.1–0.18em, `font-feature-settings: "tnum" 1, "zero" 1`): every fiscal label, every total, every nav pill, every meta strip. The mono carries data; never use it as decoration.

### Named Rules
**The Three-Job Rule.** Each typeface has one job. Big Shoulders Display declares (poster headlines, brand mark, FISCAL stamp, factura doc-type). IBM Plex Mono counts (every monetary value, every SKU, every date, every navigation pill). Sora explains (hero sub, and any longer-form body copy in future surfaces). Reassigning a face to a job it does not own breaks the system.

**The Mono Has a Reason Rule.** Mono is fiscal data, not costume. If a string has no number, date, or label attached to a number, it is not mono. The nav pill is mono because it is a control. The footer is mono because it carries version metadata. A long paragraph in mono is a fail.

## Layout

The page is a mural: one viewport, one composition. The container is centered at `max-width: 96rem` with `2.5rem` side padding at desktop, `1.5rem` at tablet, `1.25rem` at phone. The hero is a two-column grid (`1.05fr` / `1fr`) with a `4rem` gap; it collapses to a single column at `max-width: 960px` and below.

Vertical rhythm: top bar (`1.5rem` padding, `1px` paper-line-soft bottom hairline), hero (`4rem` top / `2.5rem` bottom), billing block (`1.5rem` padding bracketed by 1.5px paper-line hairlines top and bottom), footer (`2rem` top / `2.5rem` bottom). The mural reads top-down as four horizontal bands: top bar → hero → billing → footer. Each band is full-bleed within the container; the wall runs the full viewport.

Layering: the legacy ghost is absolutely positioned over the entire `.wall` at `z-index: 0` with a linear mask that fades from solid at the top to transparent at 75% of the height. The hero sits on `z-index: 1`, the top bar on `z-index: 2`. The factura sits on `z-index: 1` inside its stage; its amber shadow sits on `z-index: 0` (offset 1.4rem / 1.4rem).

## Elevation & Depth

Depth in this world is hard offset shadow, not soft blur. The factura has a 1.4rem / 1.4rem amber slab behind it (a translated, slightly-blurred copy of itself in `--amber`). The primary CTA, on hover, lifts 2px in each direction and reveals a 4px / 4px ink slab (no blur). The ghost CTA, on hover, reveals a 4px / 4px amber slab. There is no soft ambient shadow anywhere; depth is always a colored block under a surface, never a gray halo.

### Shadow Vocabulary
- **Factura slab** (background: `--amber`, `transform: translate(1.4rem, 1.4rem)`, `filter: blur(0.5px)`): the painted factura's hard offset shadow. Amber against ink.
- **CTA hover slab** (`box-shadow: 4px 4px 0 var(--ink)`): the primary CTA's hover state. Paint swap (amber → paper) plus an ink slab; surface translates -2px / -2px.
- **Ghost CTA hover slab** (`box-shadow: 4px 4px 0 var(--amber)`): the ghost CTA's hover state. Paint swap (transparent → paper) plus an amber slab.

**The Hard-Offset Rule.** Depth is a colored block under a surface, never a soft halo. A zero-blur offset shadow (`4px 4px 0`) on hover is the only sanctioned depth idiom. Soft drop shadows, ambient glows, and 1px borders under wide shadows are out of the world.

## Shapes

The form language is sharp. Every container, button, nav pill, billing item, and the factura itself uses 90° corners. The only rounded element in the system is the FISCAL stamp, which is a perfect circle (`border-radius: 50%`, 4.6rem diameter at desktop, 3.6rem on phones) rotated -14° with a 1px inner ring.

Borders are ink hairlines (`1.5px` solid `--ink`) on the paper factura, and paper-line hairlines (`1px` solid `rgba(241, 234, 214, 0.18)`) on the wall. The top bar has a faint hairline divider (`1px` solid `rgba(241, 234, 214, 0.10)`). The billing block is bracketed by 1.5px paper-line hairlines top and bottom. The declaration is preceded by a 2px amber top-border. No element uses a colored `border-left` or `border-right` above 1px.

**The Sharp-By-Default Rule.** Every container, button, and field is 90° corners. The FISCAL stamp is the only rounded element. Card radii (12–16px) and pill radii are not in this world.

## Components

### Buttons
- **Shape:** sharp 90° corners, 1.5px border, mono typography.
- **Primary (`.cta`):** amber background, ink text, amber border. Hover swaps to paper background, adds 4px / 4px 0 ink offset shadow, translates -2px / -2px. The trailing arrow (`.cta-arrow`) slides 4px right on hover.
- **Ghost (`.cta-ghost`):** transparent background, paper text, paper-line border. Hover swaps to paper background, ink text, 4px / 4px 0 amber offset shadow.
- **Focus-visible:** 2px amber outline, 3px offset. Same for the nav pill.
- **Motion:** all hover transitions are 0.15s linear (browser default easing). Reduced-motion preference disables them.

### Nav Pills (`.nav-pill`)
- **Shape:** sharp 90° corners, 1px paper-line border, mono uppercase at 0.72rem with 0.1em letter-spacing.
- **Color:** paper-soft text on the wall; hovers to amber text and amber border.
- **Used for:** the "Entrar" pill in the top bar and the per-user sign-out pill (with an inline override for a transparent background and paper-line border).

### Top Bar (`.topbar`)
- **Layout:** flex with `justify-content: space-between`, gap 2rem, padding 1.5rem 2.5rem, bottom hairline (`1px` solid `--paper-line-soft`).
- **Brand (`.brand`):** 1.9rem custom SVG mark (two triangles — cream on the left, amber on the right) + "Tetra" wordmark in display face, weight 800, 1.4rem, uppercase.
- **Top-bar meta (`.topbar-meta`):** flex of three data points (Vol/Edición/Tipo) in mono at 0.65rem, paper-faint text, paper-soft values, uppercase, 0.14em letter-spacing. Hidden under 960px.

### Hero Text (`.hero-text`)
- **Title (`.hero-title`):** Big Shoulders Display, weight 900, `clamp(4.5rem, 12vw, 11rem)`, line-height 0.82, letter-spacing -0.035em.
- **Sub (`.hero-sub`):** Sora, 0.98rem, paper-soft, max-width 30rem.
- **Declaration (`.declaration`):** display face, weight 800, `clamp(1.5rem, 2.6vw, 2.4rem)`, line-height 1.05, 2.5rem top margin, 2px amber top border, 1.5rem top padding. `<em>` for "se diseña" is amber weight 900. `<span class="strike">` for "se sufre" is paper-faint with a 3px stamp-red line-through.

### The Painted Factura (`.factura`)
- **Shape:** paper background, 1.5px ink border, mono typography, tabular numbers, 1.5rem / 1.6rem padding. Sits on a `.factura-shadow` amber slab translated 1.4rem / 1.4rem.
- **Head:** "Factura" doc-type in display face, weight 800, 1.7rem; meta strip on the right (N° / Fecha / Serie) in mono 0.7rem.
- **Blocks:** two-column grid (emisor / cliente) with `factura-label` (0.58rem mono, 0.18em tracking, ink-60%) and `factura-value` (0.76rem). Dim variants use `rgba(14, 14, 16, 0.65)`.
- **Items table:** SKU / Descripción / Cant. / P. Unit. / Total; numeric columns right-aligned; SKU dimmed; 0.55rem mono headers; 1px ink hairlines between rows.
- **Totals:** right-aligned 65%-width column; rows in mono 0.76rem with hairline separators. The `total` row is weight 700, 1.02rem, with a 2px ink border above and below and an amber-deep value. Two `bcv` rows beneath carry the BCV rate and the bolívar total at 0.68rem, no border.
- **Foot:** mono 0.6rem, paper-line hairline, uppercase, 0.12em tracking.
- **FISCAL Stamp (`.factura-stamp`):** 4.6rem circle, 3px stamp-red border, inner 1px ring, display-face text at 0.75rem, rotated -14°, opacity 0.92. Bottom-right of the factura.

### Billing Block (`.billing`)
- **Layout:** full-bleed band, 1.5px paper-line hairlines top and bottom, flex wrap with `0.5rem 1.6rem` gap, centered.
- **Item:** a 0.42rem paper-soft dot + a mono uppercase label at 0.72rem, 0.1em letter-spacing.
- **Variants:** `.amber` paints the dot and text amber (Productos, Ventas, Almacenes, Facturación fiscal, Clientes, Reportes). `.stamp` paints the dot and text fiscal red (SENIAT). Default items are paper-soft (Multi-moneda VES/USD, IGTF, Self-hosted, Código abierto).

### Footer (`.foot`)
- **Layout:** flex with `justify-content: space-between`, 2rem / 2.5rem padding, mono 0.7rem uppercase paper-faint.
- **Content:** "Tetra · Pintado para PyMEs venezolanas" on the left; "v0.1 · Hecho en Venezuela" on the right. Brand strong in paper-soft, version mono paper-faint.

### Legacy Ghost (`.legacy-ghost`) — the one authored moment
- **Layer:** absolute over `.wall`, inset 0, z-index 0, opacity 0.18 at rest.
- **Pattern:** `radial-gradient(circle, var(--paper-faint) 0.9px, transparent 1.4px)` at 5px / 5px tile. Reads as dot-matrix residue.
- **Mask:** linear gradient from solid at the top to transparent at 75% of the height (fades downward).
- **Motion:** `transition: opacity 0.5s ease`; scroll handler toggles `.is-faded` (opacity 0.05) when `scrollY > innerHeight * 0.35`. rAF-throttled. Respects `prefers-reduced-motion: reduce` (skips the listener entirely).

### Brand Mark (`.brand-mark` SVG)
- 1.9rem square SVG inside the brand slot. Two triangles forming a stylised "T" in the brand colors: cream on the left (`fill: #f1ead6`), amber on the right (`fill: #e0a020`). Source the vector; do not recreate as text.

## Do's and Don'ts

### Do
- **Do** keep the wall flat: page background is `--ink`. No gradients on the body.
- **Do** use Big Shoulders Display only for declarations, wordmarks, the factura doc-type, and the FISCAL stamp. Other uses break the three-job rule.
- **Do** use IBM Plex Mono with `font-feature-settings: "tnum" 1, "zero" 1` for every monetary value, date, SKU, and label. Tabular numbers keep the columns aligned.
- **Do** keep depth as a hard offset shadow (4px / 4px 0 or 1.4rem / 1.4rem). No soft drop shadows.
- **Do** anchor every Spanish-facing surface in `es-VE` and write copy first, translate never.
- **Do** let the legacy ghost be the only motion. New animations need a world reason; default to no.
- **Do** use the full token library (`--ink-soft`, `--ink-deep`, `--amber-glow`, `--amber-shadow`, `--stamp-deep` are reserved for future surfaces — define them once, inherit them everywhere).

### Don't
- **Don't** round anything except the FISCAL stamp. Buttons, nav pills, cards, the factura: 90° corners.
- **Don't** use fiscal red outside the FISCAL stamp. No red buttons, red borders, red lines.
- **Don't** put a kicker, eyebrow, or section number above a heading. The display face carries the weight on its own.
- **Don't** introduce glass, blur, or `backdrop-filter` as decoration. The wall is matte.
- **Don't** use Tailwind utility chains in component CSS — write the world in semantic class names (`.cta`, `.factura`, `.declaration`). Tailwind v4 is loaded for the `@source` path only.
- **Don't** ship a 1px border under a soft shadow. That is the ghost card and it is not in this world.
- **Don't** switch the wall to a light theme or alternate palette. The wall is the night wall; alternate themes break the mural.
- **Don't** close the open product decisions from `PRODUCT.md` (final OSS license, role model, sucursales, inventory costing, direct SENIAT integration, offline depth, legacy importers, cloud pricing, tenant identification) by inventing UI for them. They are listed under the Overview and future work must not silently close them.

## Implementation Status

The current built world (one page, `templates/welcome.html`, served from the existing Masonite route) ships the welcome mural as a single screen. Component-by-component status:

| Ingredient | Status |
|---|---|
| `.wall` (night wall background) | Present |
| `.legacy-ghost` + scroll fade | Present (motion idiom) |
| `.topbar` (brand + meta + nav) | Present |
| `.brand` wordmark + `.brand-mark` SVG | Present |
| `.topbar-meta` (Vol/Edición/Tipo) | Present, hidden < 960px |
| `.topbar-nav` (Entrar / Crear mi negocio →) | Present, links to `/login` and `/register` |
| `.hero` two-column layout | Present |
| `.hero-title` (TETRA wordmark) | Present |
| `.hero-sub` (Spanish product description) | Present |
| `.declaration` ("se diseña / se sufre") | Present |
| `.hero-cta` (Crear mi negocio + Iniciar sesión) | Present, links to `/register` and `/login` |
| `.factura-stage` + `.factura-shadow` amber slab | Present |
| `.factura` (painted invoice card) | Present (sample data — not generated) |
| `.factura-stamp` (FISCAL circle) | Present |
| `.billing` block (11 feature pills) | Present |
| `.foot` (Pintado para PyMEs venezolanas) | Present |
| `tailwindcss` import + `@source` directive | Present (in `resources/css/app.css`) |
| Bunny fonts CDN (Big Shoulders Display / Sora / IBM Plex Mono) | Present |
| `/register` and `/login` destination pages | **Stub** — routes exist (`routes/web.py` per `PRODUCT.md` § Evidence on Hand) but the current handlers redirect without rendering views; per `PRODUCT.md` the auth views are not yet built |
| `/logout` form | **Stub** — route exists, behavior is placeholder |
| Login, register, forgot/reset, verify email screens | **Deferred** — not designed, not built |
| Dashboard, ERP modules (Productos, Ventas, Almacenes, Facturación, Clientes, Reportes) | **Deferred** — see "Open product decisions" in Overview |
| Fiscal pricing tiers, plan badges, comparison tables | **Deferred** — out of scope until managed-cloud pricing is decided |
| Per-tenant theming, light theme, role theming | **Deferred** — the world is committed dark/ink; alternate themes would break the mural |
| Reserved tokens (`--ink-soft`, `--ink-deep`, `--amber-glow`, `--amber-shadow`, `--stamp-deep`) | **Defined, unused in v1** — the pattern vocabulary future surfaces inherit |
