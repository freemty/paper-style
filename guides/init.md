# Init Guide — Scaffold Paper Project

## Execution guidance

You are setting up a new paper project with the Paper Style theme system.

### Arguments

- `--theme NAME`: one of red, blue, gold, green, purple. Default: red.
- `--inject`: if present, skip mystyle.cls (see guides/inject.md instead).

### Steps

1. **Choose target and mode.** Use the explicit task location first, otherwise the
   existing `paper/`, or a new `paper/`. A supplied venue template wins over the
   personal report class. For palette-only integration read `guides/inject.md`.

2. **Preflight all destinations.** The initializer checks LaTeX files AND Python
   files before writing. Identical files are a no-op. If differing files conflict,
   reuse existing authorization when it covers them; otherwise ask only about
   those concrete conflicts. Never silently overwrite user palette code.

3. **Initialize through the bundled script:**

   ```bash
   python3 <paper-style>/scripts/init_paper_style.py <paper-dir> --python-dir <project-root> --theme blue
   ```

   This copies `colors.tex`, `mystyle.cls`, the legacy `preamble.tex` entry plus
   its common/class-specific components, `paper_palette.py`, and `academic.mplstyle`.
   It stages writes after a complete preflight and rolls back changed file contents
   on an ordinary write failure. This is not a crash-atomic multi-file transaction.
   `--force` is only for authorized replacement of the managed regular files;
   symlink/file-type conflicts are never followed. Back up user customizations
   before a requested overwrite if their recovery matters.

4. **Verify theme.** The script sets both the LaTeX theme and Python default to
   the same selected value; inspect their agreement.

5. **Integrate only in scope.** For a new personal report, use `mystyle` and load
   `colors` then `preamble` in the main source. Do not replace existing main files.
   This class captures the abstract before drawing its title block: place the
   `abstract` environment before `\maketitle`. Preserve that legacy contract.

6. **Validate the result.** Build with the project's engine, inspect logs and PDF
   pages, and compare any existing baseline. Record missing toolchain dependencies
   without silently installing a full TeX distribution.

7. **Report success.** Print:
   ```
   Paper Style initialized with {theme} theme.

   LaTeX: Add \input{colors} and \input{preamble} to your main.tex
   Python: from paper_palette import apply_theme
   Style:  plt.style.use("academic.mplstyle")

   Switch themes: use Paper Style's guard mode with "switch to blue".
   ```
