"""
4-panel demo figure for paper-style themes.

Usage:
    python figure_demo.py [theme_name]

theme_name: red (default), blue, gold, green, purple
Output: figure_demo_{theme}.pdf
"""

import sys
import os

# Add templates dir so paper_palette can be imported directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "templates"))

import numpy as np
import matplotlib.pyplot as plt
from paper_palette import apply_theme, get_colormap

# ── CLI arg ────────────────────────────────────────────────────────────────
theme_name = sys.argv[1] if len(sys.argv) > 1 else "red"
theme = apply_theme(theme_name)
cmap = get_colormap(theme_name)

# ── Sample data ────────────────────────────────────────────────────────────
rng = np.random.default_rng(42)
x = np.linspace(0, 2 * np.pi, 80)

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle(f"Paper Style — {theme_name.capitalize()} Theme", fontsize=13, y=1.01)

# ── Panel 1: line chart ────────────────────────────────────────────────────
ax = axes[0, 0]
colors = [theme["primary"], theme["accent"], theme["secondary"]]
for i, (label, c) in enumerate(zip(["Method A", "Method B", "Baseline"], colors)):
    noise = rng.normal(0, 0.15, len(x))
    ax.plot(x, np.sin(x - i * 0.4) + noise, color=c, lw=1.6, label=label)
ax.set_title("Line Chart")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.legend()

# ── Panel 2: bar chart ─────────────────────────────────────────────────────
ax = axes[0, 1]
categories = ["Align", "Aesth.", "Div.", "Consist."]
vals_a = rng.uniform(0.60, 0.90, len(categories))
vals_b = rng.uniform(0.55, 0.85, len(categories))
bar_w = 0.35
idx = np.arange(len(categories))
ax.bar(idx - bar_w / 2, vals_a, bar_w, color=theme["primary"], label="Ours", alpha=0.9)
ax.bar(idx + bar_w / 2, vals_b, bar_w, color=theme["muted"],   label="Base", alpha=0.9)
ax.set_xticks(idx)
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 1.05)
ax.set_title("Bar Chart")
ax.set_ylabel("Score")
ax.legend()

# ── Panel 3: heatmap ───────────────────────────────────────────────────────
ax = axes[1, 0]
data = rng.uniform(0, 1, (8, 8))
im = ax.imshow(data, cmap=cmap, aspect="auto", vmin=0, vmax=1)
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
ax.set_title("Heatmap")
ax.set_xlabel("Token Index")
ax.set_ylabel("Layer")
ax.grid(False)

# ── Panel 4: multi-line with fill ─────────────────────────────────────────
ax = axes[1, 1]
steps = np.arange(0, 100)
for i, (label, c) in enumerate(zip(["FID", "CLIP", "IS"], colors)):
    mean = np.cumsum(rng.normal(0, 0.3, len(steps))) * 0.05 + (i + 1) * 0.5
    std  = np.abs(rng.normal(0, 0.05, len(steps))) + 0.02
    ax.plot(steps, mean, color=c, lw=1.5, label=label)
    ax.fill_between(steps, mean - std, mean + std, color=c, alpha=0.15)
ax.set_title("Multi-line + CI")
ax.set_xlabel("Iteration")
ax.set_ylabel("Metric")
ax.legend()

plt.tight_layout()
out = f"figure_demo_{theme_name}.pdf"
fig.savefig(out)
print(f"Saved: {out}")
