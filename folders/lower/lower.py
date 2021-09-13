#!/usr/bin/env python3

"""
This program converts file and folder names in the folder tree starting at the
current directory or the directory specified as first command line argument to
lower case
"""

import os
import sys

from typing import List


def get_to_lower(folder: str) -> List[str]:
    """
    get files and folders that need to be converted to lowercase,
    starting at folder
    """

    to_lower = []
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        if root != root.lower():
            to_lower.append(root)
        for file in sorted(files):
            if file != file.lower():
                to_lower.append(os.path.join(root, file))
    return to_lower


def get_collisions(folder: str, to_lower: List[str]) -> List[str]:
    """
    check if renaming folders and files would create name collisions with
    existing files; return a list of name collisions
    """

    collisions = []
    lowered = [f.lower() for f in to_lower]

    for root, _dirs, files in os.walk(folder):
        if root in lowered:
            collisions.append(root)
        for file in files:
            if os.path.join(root, file) in lowered:
                collisions.append(os.path.join(root, file))
            if os.path.join(root.lower(), file) in lowered:
                collisions.append(os.path.join(root, file))
    return collisions


def main():
    """
    main entry point
    """

    to_lower = []
    if len(sys.argv) >= 2:
        # use folder specified by user
        to_lower = get_to_lower(sys.argv[1])
    else:
        # fall back to current directory
        to_lower = get_to_lower(os.curdir)

    for file in to_lower:
        print(file)


if __name__ == '__main__':
    main()
