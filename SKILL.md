---
name: paper-style
description: >
  Use when writing academic papers, creating paper figures, switching paper
  color themes, or setting up a new paper project with consistent visual identity.
  Triggers: /paper-style, paper theme, 论文配色, 画图风格, 论文模板.
---

# Paper Style — Academic Color Theme System

5 low-saturation themes (red/blue/gold/green/purple) for unified LaTeX + matplotlib visual identity.

## Choose the scope

- Personal technical report: `init` may use the licensed `mystyle.cls` and its report preamble.
- Existing venue/manuscript: preserve class, fonts, margins, anonymity, bibliography and build configuration. Use `init --inject` only when a palette change is requested.
- Figures/theme maintenance: `guard` follows the existing visual system. Ordinary prose editing does not authorize introducing a palette or replacing a template.

## Modes

| Command | Guide | What it does |
|---------|-------|-------------|
| `init [--theme NAME] [--inject]` | `guides/init.md` | Scaffold personal report, or inject palette only |
| `guard` (default) | `guides/guard.md` | Detect theme, assist with figures/tables |

**Arguments for init:**
- `--theme NAME`: red (default), blue, gold, green, purple
- `--inject`: copy palette files only; do not modify the existing class or load report components

**Read and execute the corresponding guide file.**

## Themes

| Name | Accent | Style |
|------|--------|-------|
| `red` | `#5E3545` | Warm burgundy |
| `blue` | `#3C4A57` | Desaturated slate |
| `gold` | `#564D3D` | Warm beige |
| `green` | `#2A4438` | Deep forest |
| `purple` | `#3E2548` | Deep plum |

## Templates

| File | Purpose |
|------|---------|
| `templates/colors.tex` | 5-theme LaTeX color definitions (`\ifthenelse` switch) |
| `templates/mystyle.cls` | Document class (CC BY-SA 4.0, Palatino/XCharter) |
| `templates/preamble.tex` | Backward-compatible personal-report wrapper |
| `templates/preamble-common.tex` | Optional report packages/callouts; no class-specific title treatment |
| `templates/preamble-mystyle.tex` | Personal `mystyle` title styling; never injected into a venue template |
| `templates/paper_palette.py` | Python: `get_theme()`, `apply_theme()`, `get_colormap()`, `clean_ax()`, `theme_names()` |
| `templates/academic.mplstyle` | matplotlib: serif, 300 DPI, clean spines |

## Quick Reference — Guard Mode

**Python figures:**
```python
from paper_palette import apply_theme, get_colormap
import matplotlib.pyplot as plt
plt.style.use("academic.mplstyle")
theme = apply_theme()  # reads DEFAULT_THEME
plt.plot(x, y, color=theme["primary"])
plt.imshow(data, cmap=get_colormap())
```

**LaTeX tables:**
- Ranking: `\fst{val}` / `\snd{val}` / `\trd{val}`
- Heatmap cells: `\cellcolor{perf30}` through `\cellcolor{perf80}`
- Emphasis: `\textcolor{accent_primary}{text}`

**Theme switch** (guard mode): update `\themename` in `colors.tex` + `DEFAULT_THEME` in `paper_palette.py` atomically.

Before delivery, distinguish files initialized, theme consistency checked, build
passed and PDF visually inspected. Compile using the existing project toolchain
and inspect affected pages; a successful file copy is not layout validation.
Use `scripts/init_paper_style.py` for file setup. Host invocation syntax belongs
in the README, not in shared execution instructions.
