# Inject Guide — Add Colors to Existing Document Class

## Instructions for Claude

The user has their own `.cls` file and wants only the color system, not mystyle.cls.

### Steps

1. **Copy color files only:**
   - `colors.tex` → project's paper directory
   - `paper_palette.py` → project root
   - `academic.mplstyle` → project root

2. **Set theme** in `colors.tex` and `paper_palette.py` (same as init).

3. **Print integration instructions:**

   ```
   Color system installed. To integrate with your existing .cls:

   1. Ensure your .cls loads: \RequirePackage{xcolor} and \RequirePackage{xifthen}

   2. In your main .tex, add before \begin{document}:
      \input{colors}
      \colorlet{YourAccentName}{accent_primary}
      \hypersetup{colorlinks=true, urlcolor=accent_primary, citecolor=accent_cite}

   3. For tables: \fst{}, \snd{}, \trd{} and \cellcolor{perf30..perf80}

   4. Python: from paper_palette import apply_theme
   ```
