# Paper Style

5 low-saturation color themes for academic papers — unified LaTeX + matplotlib visual identity.

A [Claude Code](https://claude.ai/claude-code) skill that provides consistent styling from `\documentclass` to `plt.savefig`.

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

### Via Skills CLI (recommended)

```bash
npx skills add freemty/paper-style -g
```

Browse on [skills.sh](https://skills.sh/)

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

Templates work standalone — just copy what you need:

### LaTeX

```latex
% In your main.tex
\documentclass[11pt,letterpaper]{mystyle}   % or your own cls
\input{colors}
\input{preamble}
\begin{document}
  ...
\end{document}
```

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
  preamble.tex        Shared preamble (hyperref, tcolorbox, abox)
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
get_theme("red")       # {'primary': '#A72B4A', 'secondary': '#3D4F5F', ...}
apply_theme("red")     # set rcParams + return theme dict
get_colormap("red")    # LinearSegmentedColormap for heatmaps
clean_ax(ax)           # remove top/right spines
```

## License

- `mystyle.cls`: CC BY-SA 4.0 (inherited from DeepMind/Berkeley template)
- Everything else: MIT
