"""Greetings with command line arguments"""

import argparse


def main():
    """main entry point"""
    parser = argparse.ArgumentParser(
        prog='greet',
        description='Print a greeting')
    parser.add_argument("-n", "--name", default="you")
    parser.add_argument("-g", "--greeting", default="hi")
    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")


if __name__ == "__main__":
    main()
