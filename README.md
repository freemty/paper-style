# Paper Style

5 low-saturation color themes for academic papers — unified LaTeX + matplotlib visual identity.

A portable Agent Skill for consistent styling from LaTeX to matplotlib. Personal
technical reports and palette-only integration into an existing venue template
are separate paths; a prose edit does not automatically adopt a new style.

## Preview

See [`examples/all_themes_preview.pdf`](examples/all_themes_preview.pdf) for all 5 themes (paper + figures).

| Theme | Accent | Best for |
|-------|--------|----------|
| **Red** (Burgundy) | `#5E3545` | Warm, authoritative papers |
| **Blue** (Slate) | `#3C4A57` | Cool, academic tone |
| **Gold** (Beige) | `#564D3D` | Warm, understated style |
| **Green** (Forest) | `#2A4438` | Deep, natural feel |
| **Purple** (Plum) | `#3E2548` | Rich, distinctive identity |

## Install

### Via skills.sh (recommended)

```bash
npx skills add freemty/paper-style -g
```

Works with Claude Code, Cursor, Codex, Windsurf, and [15+ other agents](https://skills.sh).

### Via git clone

```bash
git clone https://github.com/freemty/paper-style.git ~/.claude/skills/paper-style
```

### Check for updates

```bash
npx skills check
npx skills update
```

## Usage with Claude Code

```
/paper-style init --theme blue        # Scaffold a new paper project
/paper-style init --inject            # Inject colors into existing cls
/paper-style                          # Style guardian mode (figures, tables, theme switch)
```

## Usage without Claude Code

Codex: `$paper-style`. Other hosts: use the skill selector or ask naturally.

Safe deterministic initialization:

```bash
python3 scripts/init_paper_style.py paper --python-dir . --theme blue
python3 scripts/init_paper_style.py paper --python-dir . --theme blue --inject
```

All destinations are checked before writes, identical files are a no-op, and
conflicts require explicit resolution. `--force` replaces only managed regular
files; it never follows destination symlinks. Keep backups for customized files.
The operation rolls back file contents on ordinary write errors, but cannot
promise multi-file crash atomicity.

Templates work standalone — just copy what you need:

### LaTeX

```latex
% In your main.tex
\documentclass[11pt,letterpaper]{mystyle}   % personal report, not a venue replacement
\input{colors}
\input{preamble}
\begin{document}
  \begin{abstract}Your abstract, captured before the title block.\end{abstract}
  \maketitle
  ...
\end{document}
```

For an existing venue class, use `--inject`, keep the original `\documentclass`,
and add only `\input{colors}` plus requested color uses to the main source.
Do not load the report preamble, edit vendor class files, or change font/margins,
anonymity, bibliography or link policy. Check name collisions and venue rules,
then build and visually compare affected pages. Palette initialization is not
venue certification or visual QA.

Switch themes by editing one line in `colors.tex`:

```latex
\newcommand{\themename}{blue}   % red | blue | gold | green | purple
```

### Python (matplotlib)

```python
from paper_palette import apply_theme, get_colormap
import matplotlib.pyplot as plt

plt.style.use("academic.mplstyle")
theme = apply_theme("blue")

# Line chart
plt.plot(x, y, color=theme["primary"])

# Heatmap
plt.imshow(data, cmap=get_colormap("blue"))

# Bar chart
plt.bar(labels, values, color=[theme["primary"], theme["secondary"]])
```

### LaTeX Tables

```latex
% Ranking highlights (1st/2nd/3rd)
\fst{0.95}  \snd{0.91}  \trd{0.88}

% Heatmap cells (perf0=white → perf80=dark)
\cellcolor{perf60} 0.87
```

## What's Included

```
templates/
  colors.tex          5-theme LaTeX color definitions
  mystyle.cls         Document class (Palatino/XCharter, CC BY-SA 4.0)
  preamble.tex        Legacy personal-report entry
  preamble-common.tex Optional report components
  preamble-mystyle.tex Personal title treatment
  paper_palette.py    Python theme module (zero deps at import)
  academic.mplstyle   matplotlib style (serif, 300 DPI, clean spines)

examples/
  figure_demo.py      4-panel figure demo
  table_demo.tex      Table color usage demo
  all_themes_preview.pdf   Visual preview of all 5 themes
```

## Python API

```python
from paper_palette import get_theme, apply_theme, get_colormap, clean_ax, theme_names

theme_names()          # ['red', 'blue', 'gold', 'green', 'purple']
get_theme("red")       # copy of the existing named theme dictionary
apply_theme("red")     # set rcParams + return theme dict
get_colormap("red")    # LinearSegmentedColormap for heatmaps
clean_ax(ax)           # remove top/right spines
```

## Verification

```bash
python3 tests/test_init.py
```

The parent yuanbo-skills repository additionally runs real TeX/PDF checks with
an authored venue fixture and the personal report. Actual venue releases still
need their own current template checks; those are not simulated by the fixture.

## License

- `mystyle.cls`: CC BY-SA 4.0 (inherited from DeepMind/Berkeley template)
- Everything else: MIT
