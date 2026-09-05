"""File safety and theme consistency at the public initializer boundary."""
from pathlib import Path
import subprocess
import importlib.util
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "init_paper_style.py"


class InitTests(unittest.TestCase):
    def run_init(self, root, *args):
        return subprocess.run([sys.executable, str(SCRIPT), str(root / "paper"), "--python-dir", str(root), *args], text=True, capture_output=True)

    def test_python_conflict_prevents_all_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertTrue(SCRIPT.is_file(), "initializer is not implemented")
            (root / "paper_palette.py").write_text("user code")
            result = self.run_init(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sorted(p.name for p in root.iterdir()), ["paper_palette.py"])

    def test_inject_preserves_venue_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "paper").mkdir()
            for name in ("venue.cls", "main.tex", "references.bib"):
                (root / "paper" / name).write_text("user " + name)
            result = self.run_init(root, "--inject", "--theme", "blue")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((root / "paper/mystyle.cls").exists())
            self.assertFalse((root / "paper/preamble.tex").exists())
            for name in ("venue.cls", "main.tex", "references.bib"):
                self.assertEqual((root / "paper" / name).read_text(), "user " + name)
            self.assertIn(r"\newcommand{\themename}{blue}", (root / "paper/colors.tex").read_text())
            self.assertIn('DEFAULT_THEME = "blue"', (root / "paper_palette.py").read_text())
            before = {p: p.stat().st_mtime_ns for p in root.rglob("*") if p.is_file()}
            repeat = self.run_init(root, "--inject", "--theme", "blue")
            self.assertEqual(repeat.returncode, 0, repeat.stderr)
            self.assertEqual(before, {p: p.stat().st_mtime_ns for p in before})

    def test_force_never_follows_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertTrue(SCRIPT.is_file(), "initializer is not implemented")
            outside = root / "outside.py"
            outside.write_text("untouched")
            (root / "paper_palette.py").symlink_to(outside)
            result = self.run_init(root, "--force")
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(outside.read_text(), "untouched")
            self.assertFalse((root / "paper").exists())

    def test_all_theme_selections_reach_latex_and_python(self):
        for theme in ("red", "blue", "gold", "green", "purple"):
            with self.subTest(theme=theme), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                result = self.run_init(root, "--theme", theme)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(r"\newcommand{\themename}{" + theme + "}", (root / "paper/colors.tex").read_text())
                spec = importlib.util.spec_from_file_location("palette", root / "paper_palette.py")
                palette = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(palette)
                self.assertEqual(palette.DEFAULT_THEME, theme)
                self.assertEqual(palette.get_theme(), palette.get_theme(theme))
                for name in ("preamble.tex", "preamble-common.tex", "preamble-mystyle.tex", "mystyle.cls"):
                    self.assertTrue((root / "paper" / name).is_file())


if __name__ == "__main__":
    unittest.main()
