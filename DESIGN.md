---
name: Keystone Starter Kit
description: Modern developer-first Masonite 5 starter kit with Vite and Tailwind CSS v4
colors:
  primary: "#6d4fe3"
  primary-dark: "#9c82f2"
  accent-strong: "#4a33a6"
  neutral-bg: "#fbfaf8"
  neutral-bg-dark: "#14181e"
  neutral-fg: "#14181e"
  neutral-fg-dark: "#e6e8eb"
  card-bg: "#ffffff"
  card-bg-dark: "#1c2128"
  muted: "#5e626a"
  muted-dark: "#9aa0a8"
typography:
  display:
    fontFamily: "Sora, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2.25rem, 5vw, 3.25rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Sora, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "0.25rem"
  md: "0.75rem"
  full: "999px"
spacing:
  sm: "0.75rem"
  md: "1.5rem"
  lg: "3rem"
components:
  card:
    backgroundColor: "{colors.card-bg}"
    textColor: "{colors.neutral-fg}"
    rounded: "{rounded.md}"
    padding: "1.5rem"
  pill:
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "0.15rem 0.75rem"
---

# Design System: Keystone Starter Kit

## 1. Overview

**Creative North Star: "The Solid Foundation"**

Keystone's design system delivers a clean, developer-focused aesthetic for Masonite 5 applications. Built around high-contrast typography, refined layout rhythm, and subtle violet accents, the system balances expert confidence with approachable simplicity.

Key Characteristics:
- Dual-mode dark/light adaptability with smooth color transitions.
- High-readability typography using Sora for headings and body text.
- Micro-interactions focused on slight elevation and hover feedback.

## 2. Colors

A deliberate, low-chroma neutral palette paired with a vibrant deep violet accent.

### Primary
- **Masonite Violet** (`#6d4fe3` / dark `#9c82f2`): Used for primary action indicators, brand marks, focus rings, and accent text.

### Neutral
- **Surface Background** (`#fbfaf8` / dark `#14181e`): Crisp, glare-free background surface.
- **Card Surface** (`#ffffff` / dark `#1c2128`): High-clarity container surface.
- **Foreground Ink** (`#14181e` / dark `#e6e8eb`): High-contrast body text ensuring >= 4.5:1 contrast ratio.
- **Muted Text** (`#5e626a` / dark `#9aa0a8`): Secondary labels and metadata.

### Named Rules
**The Single Accent Rule.** Violet is reserved for interactive affordances and key focal points, carrying <= 15% of any screen surface.

## 3. Typography

**Display & Body Font:** Sora (with ui-sans-serif fallback)

### Hierarchy
- **Display** (600, `clamp(2.25rem, 5vw, 3.25rem)`, 1.15): Hero headers and major section titles.
- **Headline** (600, 1.25rem, 1.2): Component and card titles.
- **Body** (400, 1rem, 1.6): Paragraph prose and descriptions. Max line-length 65-75ch.
- **Label** (500, 0.8rem, 1.4): Version badges, pills, and code tags.

## 4. Elevation

Keystone relies on crisp 1px borders and subtle background radial glows rather than heavy drop shadows.

### Named Rules
**The Border-First Elevation Rule.** Depth is established via subtle border lines (`rgba(20, 24, 30, 0.12)`) and background contrast rather than diffuse drop shadows.

## 5. Components

### Cards
- **Shape:** Rounded medium (`0.75rem` / `12px`)
- **Background:** `--card` surface
- **Border:** 1px subtle stroke (`--border`)
- **Hover:** Border color shifts to Masonite Violet (`--accent`), subtle `-2px` Y-axis lift.

### Pills / Badges
- **Shape:** Full pill (`999px`)
- **Border:** 1px solid `--accent`
- **Text:** `--accent`, font weight 500.

## 6. Do's and Don'ts

### Do:
- **Do** maintain strict contrast standards for body and placeholder text.
- **Do** use responsive container grids (`repeat(auto-fit, minmax(16rem, 1fr))`).
- **Do** respect `prefers-reduced-motion` for all hover and reveal transitions.

### Don't:
- **Don't** use generic corporate SaaS templates, heavy bootstrap dashboards, or bloated AI-generated UI elements.
- **Don't** pair 1px solid borders with wide drop shadows (M >= 16px).
- **Don't** use colored side-stripe borders or gradient background text clips.
