"""
lower test cases
"""

import os
import tempfile
import unittest

import lower


class LowerTestCase(unittest.TestCase):
    """
    lower test case
    """

    def test_get_to_lower(self) -> None:
        """
        test function get_to_lower()
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            # create dummy file tree
            dir_a = os.path.join(tmpdir, "A")
            dir_b = os.path.join(tmpdir, "b")
            dir_c = os.path.join(tmpdir, "C")
            for folder in [dir_a, dir_b, dir_c]:
                os.mkdir(folder)
            file_1 = os.path.join(dir_a, "F1")
            file_2 = os.path.join(dir_b, "f2")
            file_3 = os.path.join(dir_b, "F3")
            for file in [file_1, file_2, file_3]:
                with open(file, "a", encoding='UTF-8'):
                    pass

            # generate and check output
            want = [dir_a, file_1, dir_c, file_3]
            got = lower.get_to_lower(tmpdir)
            self.assertEqual(got, want)
