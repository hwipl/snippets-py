"""
tree tests
"""

import io
import os
import tempfile
import unittest

import tree


class TreeTestCase(unittest.TestCase):
    """
    tree test case
    """

    def test_write_tree(self) -> None:
        """
        test walk function
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            # create dummy file tree
            dir_a = os.path.join(tmpdir, "a")
            dir_b = os.path.join(tmpdir, "b")
            dir_c = os.path.join(tmpdir, "c")
            for folder in [dir_a, dir_b, dir_c]:
                os.mkdir(folder)
            file_1 = os.path.join(dir_a, "1")
            file_2 = os.path.join(dir_b, "2")
            file_3 = os.path.join(dir_b, "3")
            for file in [file_1, file_2, file_3]:
                with open(file, "a", encoding='UTF-8'):
                    pass

            # generate and check output
            want = f"""{tmpdir}
{dir_a}
{file_1}
{dir_b}
{file_2}
{file_3}
{dir_c}
"""
            with io.StringIO() as out:
                tree.write_tree(tmpdir, out)
                self.assertEqual(out.getvalue(), want)
