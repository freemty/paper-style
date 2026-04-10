# Guard Guide — Style Guardian Mode

## Instructions for Claude

You are acting as a style guardian for an existing paper project.

### On Entry

1. **Find project theme.** Read `colors.tex` (search paper/, then root). Extract
   the `\themename` value. If not found, suggest running `/paper-style init` first.

2. **Find Python palette.** Read `paper_palette.py` (search root, then paper/).
   Check that `DEFAULT_THEME` matches LaTeX theme. If mismatch, offer to fix.

3. **Confirm.** Print: "Active theme: {name}. Ready to assist with figures and tables."

### Ongoing Assistance

When the user asks you to create figures or tables:

- **Figures:** Import from `paper_palette.py`. Use `apply_theme()` for rcParams,
  `get_theme()` for color dict, `get_colormap()` for heatmaps. Always include
  `plt.style.use("academic.mplstyle")` at the top.

- **Tables:** Use `\fst{}`, `\snd{}`, `\trd{}` for ranking. Use `\cellcolor{perf30}`
  through `\cellcolor{perf80}` for heatmap cells.

- **Theme switch:** When user says "switch to {name}":
  1. Update `\themename` in `colors.tex`
  2. Update `DEFAULT_THEME` in `paper_palette.py`
  3. Report: "Switched to {name} theme. Both LaTeX and Python updated."

### Color Quick Reference

Read the color values from the project's `paper_palette.py` (copied during init).
Do not hardcode colors — always reference the theme dict via `get_theme()`.
