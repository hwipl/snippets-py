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


def rename_files(to_lower: List[str]) -> None:
    """
    Rename all files and folders in to_lower to lower case
    """

    to_lower.sort()
    for file in to_lower:
        head, tail = os.path.split(file)
        file = os.path.join(head.lower(), tail)
        os.rename(file, file.lower())


def main():
    """
    main entry point
    """

    # use current directory or folder specified by user
    folder = os.curdir
    if len(sys.argv) >= 2:
        folder = sys.argv[1]

    # get list of files to be renamed and check name collisions
    to_lower = get_to_lower(folder)
    collisions = get_collisions(folder, to_lower)

    # abort if there are name collisions
    if len(collisions) != 0:
        print("Renaming would create collisions with the following files:")
        for file in collisions:
            print(file)
        print("Aborting.")
        return

    # abort if there are no files to rename
    if len(to_lower) == 0:
        return

    # show files to rename
    print("The following files will be renamed:")
    for file in to_lower:
        print(file)

    # ask user for permission and rename files
    rename = input("Enter 'RENAME' to continue: ")
    if rename != "RENAME":
        print("Aborting.")
        return
    rename_files(to_lower)


if __name__ == '__main__':
    main()
