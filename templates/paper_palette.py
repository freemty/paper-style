"""
Paper Style — Unified color palette for academic papers.

Provides 5 low-saturation color themes that match the LaTeX colors.tex.
Zero external dependencies at import time; matplotlib imported lazily.

Usage:
    from paper_palette import apply_theme, get_colormap
    theme = apply_theme("red")
    plt.plot(x, y, color=theme["primary"])
    plt.imshow(data, cmap=get_colormap("red"))
"""

from __future__ import annotations

_MUTED = "#8A9099"  # theme-neutral gray, shared by all themes

THEMES: dict[str, dict[str, str | list[str]]] = {
    "red": {
        "primary": "#A72B4A",
        "secondary": "#3D4F5F",
        "accent": "#D4734E",
        "muted": _MUTED,
        "deep": "#270A11",
        "indigo": "#561A29",
        "light": "#EAA8B9",
        "silver": "#EFD4DB",
        "gradient": [
            "#ffffff", "#fbf5f7", "#f5ebee", "#eee0e3", "#e8d5da",
            "#e2cbd1", "#dcc0c7", "#d5b3bb", "#cea5af",
        ],
    },
    "blue": {
        "primary": "#416991",
        "secondary": "#3C4A57",
        "accent": "#6A8FA8",
        "muted": _MUTED,
        "deep": "#0F1822",
        "indigo": "#25384C",
        "light": "#B4C9DE",
        "silver": "#D9E2EA",
        "gradient": [
            "#ffffff", "#f6f8fa", "#edf0f3", "#e2e7ec", "#d8dfe5",
            "#cfd6de", "#c5ced7", "#b9c4cf", "#acbac7",
        ],
    },
    "gold": {
        "primary": "#8E7344",
        "secondary": "#564D3D",
        "accent": "#B89A5E",
        "muted": _MUTED,
        "deep": "#211B10",
        "indigo": "#4A3D26",
        "light": "#DDCEB5",
        "silver": "#EAE4D9",
        "gradient": [
            "#ffffff", "#faf8f6", "#f3f1ed", "#ebe8e3", "#e4e0d9",
            "#ddd8d0", "#d6d0c6", "#cec7ba", "#c6bdad",
        ],
    },
    "green": {
        "primary": "#24604A",
        "secondary": "#2A4438",
        "accent": "#4A8A6A",
        "muted": _MUTED,
        "deep": "#081810",
        "indigo": "#143026",
        "light": "#A8EACF",
        "silver": "#D4EFE4",
        "gradient": [
            "#ffffff", "#f5faf8", "#ebf4f0", "#e0ede7", "#d5e6de",
            "#cbe0d6", "#c0d9cd", "#b3d1c3", "#a5c9b9",
        ],
    },
    "purple": {
        "primary": "#5C2870",
        "secondary": "#3E2548",
        "accent": "#8A5CA0",
        "muted": _MUTED,
        "deep": "#150820",
        "indigo": "#2A1238",
        "light": "#DFA8EA",
        "silver": "#EBD4EF",
        "gradient": [
            "#ffffff", "#f9f5fb", "#f2ebf5", "#ebe0ee", "#e4d5e8",
            "#ddcbe2", "#d6c0dc", "#ceb3d5", "#c6a5ce",
        ],
    },
}

DEFAULT_THEME = "red"


def theme_names() -> list[str]:
    """Return all available theme names."""
    return list(THEMES.keys())


def get_theme(name: str | None = None) -> dict[str, str | list[str]]:
    """Return a copy of the theme color dict. None uses DEFAULT_THEME."""
    key = name or DEFAULT_THEME
    if key not in THEMES:
        raise ValueError(f"Unknown theme '{key}'. Available: {theme_names()}")
    return {**THEMES[key], "gradient": list(THEMES[key]["gradient"])}


def apply_theme(name: str | None = None) -> dict[str, str | list[str]]:
    """Set matplotlib rcParams for academic style and return theme dict.

    Static rcParams here mirror academic.mplstyle; the only extra key is
    grid.color (theme-dependent). Keep both in sync when changing values.
    """
    import matplotlib.pyplot as plt

    theme = get_theme(name)
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "axes.grid": True,
        "grid.alpha": 0.15,
        "grid.linestyle": "--",
        "grid.color": theme["muted"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.fontsize": 9,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.1,
        "figure.facecolor": "white",
    })
    return theme


def get_colormap(name: str | None = None):
    """Return a LinearSegmentedColormap built from the theme's gradient."""
    import matplotlib.colors as mcolors

    key = name or DEFAULT_THEME
    theme = get_theme(key)
    return mcolors.LinearSegmentedColormap.from_list(
        f"paper_{key}", theme["gradient"], N=256
    )


def clean_ax(ax) -> None:
    """Remove top/right spines from a single axes.

    Only needed when axes was created before apply_theme(), or when using
    plt.style.use('academic.mplstyle') instead of apply_theme().
    """
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
