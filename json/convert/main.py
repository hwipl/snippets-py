#!/usr/bin/env python3

"""
This program parses a json object and converts the keys to upper case.
"""

import json

# json type
JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


def key_to_upper(obj: dict) -> dict:
    """
    convert keys in obj to upper case
    """

    new_obj = {}
    for key, value in obj.items():
        new_obj[key.upper()] = value

    return new_obj


def parse_json(s: str) -> JSON:
    """
    parse json and convert keys
    """

    return json.loads(s, object_hook=key_to_upper)


def main():
    """
    main entry point
    """

    j = parse_json('''{"name": "you", "greeting": "hi", "stuff": {"test":
                   "test"}}''')
    print(j)


if __name__ == "__main__":
    main()
