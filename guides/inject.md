# Inject Guide — Add Colors to Existing Document Class

## Execution guidance

The user has their own `.cls` file and wants only the color system, not mystyle.cls.

### Steps

1. **Run the safe initializer with `--inject`:**

   ```bash
   python3 <paper-style>/scripts/init_paper_style.py <paper-dir> --python-dir <project-root> --theme blue --inject
   ```

   It preflights all destinations and copies only:
   - `colors.tex` → project's paper directory
   - `paper_palette.py` → project root
   - `academic.mplstyle` → project root

2. **Check scope and agreement.** The script sets the theme in both files. It does
   not copy a class or preamble and does not edit the manuscript. Retain existing
   fonts, geometry, author masking, citation style, class options and hyperlink
   policy. Identical files are left unchanged; resolve actual conflicting files
   before retrying. Do not use `--force` to discard unreviewed customizations.

3. **Print integration instructions:**

   ```
   Color system installed. To integrate in your main source (not the vendor .cls):

   1. colors.tex loads its palette dependencies; it does not change the title layout.

   2. In your main .tex, add before \begin{document}:
      \input{colors}
      \colorlet{YourAccentName}{accent_primary}
      % Preserve the venue's existing hyperlink and bibliography settings.

   3. For tables: \fst{}, \snd{}, \trd{} and \cellcolor{perf30..perf80}

   4. Python: from paper_palette import apply_theme
   ```

4. **Build and compare.** If manuscript integration is authorized, add only the
   palette input and requested color uses. Inspect the same page/viewport before
   and after: layout, typeface, anonymity and citations must be unchanged.
   Check for existing macro/color-name collisions before input; do not rename
   vendor macros or overwrite an existing meaning merely to install the palette.
   Venue restrictions take precedence over personal colored tables or links.
