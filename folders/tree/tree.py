#!/usr/bin/env python3

"""
This program prints the folder tree
"""

import os
import sys


def walk(folder: str) -> None:
    """
    walk file tree
    """

    for root, dirs, files in os.walk(folder):
        dirs.sort()
        print(root)
        for file in sorted(files):
            print(os.path.join(root, file))


def main():
    """
    main entry point
    """

    # use folder specified by user
    if len(sys.argv) >= 2:
        walk(sys.argv[1])
        return

    # fall back to current directory
    walk(os.curdir)


if __name__ == '__main__':
    main()
