#!/usr/bin/env python3

"""
This program prints the folder tree
"""

import os
import sys

from typing import IO


def write_tree(folder: str, out: IO) -> None:
    """
    walk file tree starting at folder and write output to out
    """

    for root, dirs, files in os.walk(folder):
        dirs.sort()
        print(root, file=out)
        for file in sorted(files):
            print(os.path.join(root, file), file=out)


def main():
    """
    main entry point
    """

    # use folder specified by user
    if len(sys.argv) >= 2:
        write_tree(sys.argv[1], sys.stdout)
        return

    # fall back to current directory
    write_tree(os.curdir, sys.stdout)


if __name__ == '__main__':
    main()
