# Guard Guide — Style Guardian Mode

## Execution guidance

You are acting as a style guardian for an existing paper project.

### On Entry

1. **Find project theme.** Read `colors.tex` (search paper/, then root). Extract
   the `\themename` value. If absent, preserve the current visual system; suggest
   initialization only if the task actually asks to adopt Paper Style.

2. **Find Python palette.** Read `paper_palette.py` (search root, then paper/).
   Check that `DEFAULT_THEME` matches LaTeX theme. Fix within an already-authorized
   theme change; otherwise report a concrete mismatch without rewriting files.

3. **Confirm.** Print: "Active theme: {name}. Ready to assist with figures and tables."

### Ongoing Assistance

When the user asks you to create figures or tables:

- **Figures:** Import from `paper_palette.py`. Use `apply_theme()` for rcParams,
  `get_theme()` for color dict, `get_colormap()` for heatmaps. Use the project's
  `academic.mplstyle` when it is the chosen figure style, not to override a venue
  or supplied plot's typography during an unrelated edit.

- **Tables:** Use `\fst{}`, `\snd{}`, `\trd{}` for ranking. Use `\cellcolor{perf30}`
  through `\cellcolor{perf80}` for heatmap cells.

- **Theme switch:** When user says "switch to {name}":
  1. Preflight both existing files and locate their current theme declarations.
  2. Apply only the two declaration edits as one change set, preserving custom code.
  3. Verify agreement, build affected artifacts and inspect the changed pages/plots.
     Do not reinitialize customized templates merely to switch a theme.

### Color Quick Reference

Read the color values from the project's `paper_palette.py` (copied during init).
Do not hardcode colors — always reference the theme dict via `get_theme()`.
