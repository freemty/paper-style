# Init Guide — Scaffold Paper Project

## Instructions for Claude

You are setting up a new paper project with the Paper Style theme system.

### Arguments

- `--theme NAME`: one of red, blue, gold, green, purple. Default: red.
- `--inject`: if present, skip mystyle.cls (see guides/inject.md instead).

### Steps

1. **Detect target directory.** If the project has a `paper/` directory, use it.
   Otherwise ask: "Should I create a `paper/` directory, or place files in the project root?"

2. **Check for existing files.** Look for `colors.tex`, `mystyle.cls`, `preamble.tex` in the target.
   - If any exist, ask: "Found existing {files}. Overwrite, backup (.bak), or abort?"
   - Respect the user's choice.

3. **Copy LaTeX templates.** From this skill's `templates/` directory, copy to the target:
   - `colors.tex`
   - `mystyle.cls` (skip if `--inject`)
   - `preamble.tex`

4. **Set the theme.** In the copied `colors.tex`, change the `\newcommand{\themename}{...}`
   line to the requested theme name.

5. **Copy Python files.** Copy to the project root (not paper/):
   - `paper_palette.py`
   - `academic.mplstyle`

6. **Set Python default theme.** In the copied `paper_palette.py`, change
   `DEFAULT_THEME = "red"` to match the requested theme.

7. **Report success.** Print:
   ```
   Paper Style initialized with {theme} theme.

   LaTeX: Add \input{colors} and \input{preamble} to your main.tex
   Python: from paper_palette import apply_theme
   Style:  plt.style.use("academic.mplstyle")

   Switch themes: /paper-style guard → "switch to blue"
   ```
