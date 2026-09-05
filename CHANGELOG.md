# Changelog

## Unreleased — 2026-09-05

- Separate personal report, existing venue palette injection, and scoped guard modes.
- Add safe initializer with full LaTeX/Python preflight, idempotence and write-error rollback.
- Split optional common report components from `mystyle` title treatment while retaining `preamble.tex`.
- Keep palette dependencies self-contained and preserve existing logo declarations.
- Fix empty-logo handling and document the existing abstract-before-title contract.
- Verify real PDF output, existing layout/citations and theme agreement; initialization alone is not QA.

## [1.0.0] — 2026-04-10

### Added
- 5 low-saturation color themes: red (burgundy), blue (desaturated slate),
  gold (warm beige), green (deep forest), purple (deep plum)
- LaTeX templates: `colors.tex`, `mystyle.cls`, `preamble.tex`
- Python palette module: `paper_palette.py` with `get_theme()`, `apply_theme()`,
  `get_colormap()`, `clean_ax()`
- matplotlib style file: `academic.mplstyle`
- Three interaction modes: `init`, `guard`, `init --inject`
- Working examples: `figure_demo.py`, `table_demo.tex`
