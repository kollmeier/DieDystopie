"""Run with: python3 -m unittest discover -s scripts -p 'test_*.py'."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import quote


class BuildContextTest(unittest.TestCase):
    def test_templates_are_excluded_and_context_preserves_briefing(self):
        with tempfile.TemporaryDirectory(prefix='_context-test-') as temporary:
            root = Path(temporary)
            scripts = root / 'scripts'
            scripts.mkdir()
            generator = scripts / 'build_context.py'
            shutil.copyfile(Path(__file__).with_name('build_context.py'), generator)
            project = root / 'lost-tales'
            project.mkdir()
            briefing = project / 'context-briefing.md'
            original = b'# Briefing\n\nKeep this structure.\n'
            briefing.write_bytes(original)
            included = ['README.md', 'RULES.md', 'THEMES.md', 'LORE-GUARD.md', 'visual-style.md']
            excluded = []
            for section in ('strips', 'characters', 'locations', 'reference_locations'):
                included += [f'{section}/README.md',
                             f'{section}/Real_group/README.md',
                             f'{section}/Real_group/Real child/README.md']
                excluded += [f'{section}/_template/README.md',
                             f'{section}/_template/normal/README.md',
                             f'{section}/Real_group/_draft/deep/README.md']
            for relative in included + excluded:
                path = project / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('# Entry\n', encoding='utf-8')

            subprocess.run([sys.executable, str(generator)], check=True, capture_output=True)
            index = (project / 'context-index.md').read_text(encoding='utf-8')
            links = [line for line in index.splitlines() if line.startswith('- [')]
            self.assertEqual(len(links), len(included))
            for relative in included:
                self.assertIn(f']({quote(relative, safe="/.-_")})', index)
            for relative in excluded:
                self.assertNotIn(f']({quote(relative, safe="/.-_")})', index)
            self.assertEqual(briefing.read_bytes(), original)
            context = (project / 'context.md').read_text(encoding='utf-8')
            self.assertTrue(context.endswith(
                original.decode().strip() + '\n\n---\n\n' + index.strip() + '\n'))

    def test_missing_sections_are_optional(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'scripts').mkdir()
            generator = root / 'scripts' / 'build_context.py'
            shutil.copyfile(Path(__file__).with_name('build_context.py'), generator)
            project = root / 'lost-tales'
            project.mkdir()
            (project / 'context-briefing.md').write_text('# Briefing\n', encoding='utf-8')
            subprocess.run([sys.executable, str(generator)], check=True, capture_output=True)
            self.assertNotIn('## ', (project / 'context-index.md').read_text(encoding='utf-8'))
            self.assertTrue((project / 'context.md').is_file())


if __name__ == '__main__':
    unittest.main()
