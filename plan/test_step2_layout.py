"""Run with: python -m unittest discover -s plan -p 'test_*.py'."""
import pathlib
import runpy
import shutil
import tempfile
import unittest

import matplotlib.pyplot as plt
import numpy as np


class Step2DrawingTests(unittest.TestCase):
    def test_overlay_preserves_every_original_patch_and_line(self):
        source = pathlib.Path(__file__).parent
        self.assertTrue((source / 'step2_layout.py').exists(), 'Step 2 drawing is missing')
        with tempfile.TemporaryDirectory() as tmp:
            for name in ('base_plan.py', 'step2_layout.py'):
                shutil.copy(source / name, tmp)
            base = runpy.run_path(str(pathlib.Path(tmp) / 'base_plan.py'))
            step = runpy.run_path(str(pathlib.Path(tmp) / 'step2_layout.py'))
            for original, actual in zip(base['ax'].patches, step['ax'].patches):
                np.testing.assert_allclose(
                    original.get_patch_transform().transform(original.get_path().vertices),
                    actual.get_patch_transform().transform(actual.get_path().vertices),
                )
            self.assertGreater(len(step['ax'].patches), len(base['ax'].patches))
            for original, actual in zip(base['ax'].lines, step['ax'].lines):
                np.testing.assert_allclose(original.get_xydata(), actual.get_xydata())
            self.assertGreaterEqual(len(step['ax'].lines), len(base['ax'].lines))
            for name in ('step2_layout.png', 'step2_electrical.png'):
                output = pathlib.Path(tmp) / name
                self.assertTrue(output.exists(), name)
                self.assertGreater(output.stat().st_size, 100_000)
            plt.close('all')


if __name__ == '__main__':
    unittest.main()
