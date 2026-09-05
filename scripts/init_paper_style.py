#!/usr/bin/env python3
"""Initialize a report or inject a palette without editing a venue template."""
from pathlib import Path
import argparse
import os
import re
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--python-dir", type=Path, help="default: target's parent (project root)")
    parser.add_argument("--theme", choices=("red", "blue", "gold", "green", "purple"), default="red")
    parser.add_argument("--inject", action="store_true", help="palette only; no class or preamble")
    parser.add_argument("--force", action="store_true", help="replace conflicting regular managed files")
    args = parser.parse_args()
    python_arg = args.python_dir or args.target.absolute().parent
    if args.target.is_symlink() or python_arg.is_symlink():
        raise SystemExit("explicit target directories must not be symlinks")
    # Normalize OS aliases such as macOS /var -> /private/var before preflight.
    target = args.target.resolve()
    python_dir = python_arg.resolve()
    templates = Path(__file__).resolve().parents[1] / "templates"
    names = ["colors.tex"]
    if not args.inject:
        names += ["mystyle.cls", "preamble.tex", "preamble-common.tex", "preamble-mystyle.tex"]
    outputs = {target / name: (templates / name).read_bytes() for name in names}
    outputs.update({python_dir / name: (templates / name).read_bytes()
                    for name in ("paper_palette.py", "academic.mplstyle")})
    outputs[target / "colors.tex"] = re.sub(
        rb"(?m)^\\newcommand\{\\themename\}\{red\}",
        lambda _: (r"\newcommand{\themename}{" + args.theme + "}").encode(),
        outputs[target / "colors.tex"], count=1)
    outputs[python_dir / "paper_palette.py"] = outputs[python_dir / "paper_palette.py"].replace(
        b'DEFAULT_THEME = "red"', f'DEFAULT_THEME = "{args.theme}"'.encode(), 1)

    original = {}
    for path, data in outputs.items():
        for parent in path.parents:
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise SystemExit(f"refusing non-directory or symlink parent: {parent}")
        if path.is_symlink() or (path.exists() and not path.is_file()):
            raise SystemExit(f"refusing non-regular destination: {path}")
        original[path] = path.read_bytes() if path.exists() else None
        if original[path] is not None and original[path] != data and not args.force:
            raise SystemExit(f"conflict: {path}; nothing changed. Resolve it or authorize --force.")

    changed = {path: data for path, data in outputs.items() if original[path] != data}
    staged = {}
    replaced = []
    try:
        for path, data in changed.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, filename = tempfile.mkstemp(prefix=".paper-style-", dir=path.parent)
            staged[path] = Path(filename)
            with os.fdopen(fd, "wb") as stream:
                stream.write(data)
            staged[path].chmod(path.stat().st_mode & 0o777 if path.exists() else 0o644)
        for path in changed:
            if path.is_symlink() or (path.read_bytes() if path.exists() else None) != original[path]:
                raise OSError(f"destination changed during initialization: {path}")
        for path, stage in staged.items():
            os.replace(stage, path)
            replaced.append(path)
    except OSError:
        for path in reversed(replaced):
            if original[path] is None:
                path.unlink()
            else:
                path.write_bytes(original[path])
        raise
    finally:
        for stage in staged.values():
            if stage.exists():
                stage.unlink()
    print(f"Paper Style {args.theme}: {len(changed)} files updated; venue/source files were not edited.")
    print(r"LaTeX: \input{colors}" + ("" if args.inject else r" then \input{preamble} (personal report only)."))
    print(f"Python palette: {python_dir / 'paper_palette.py'}")
    print("Review/build/visual checks remain pending; initialization is not artifact approval.")


if __name__ == "__main__":
    main()
