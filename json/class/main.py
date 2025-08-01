#!/usr/bin/env python3

"""
This program (de)serializes a class to json string.
"""

import json

# data type
DATA = str | int | list[str] | dict[str, str]


class Data:
    """Data class"""

    def __init__(self, **kwargs: DATA) -> None:

        # default values
        self.str_field: str = ""
        self.int_field: int = 0
        self.list_field: list[str] = []
        self.dict_field: dict[str, str] = {}

        # set fields from arguments
        self.set_fields(**kwargs)

    def set_fields(self, **kwargs: DATA) -> None:
        """set data fields from arguments"""

        for key, value in kwargs.items():
            match key:
                case "str_field":
                    if not isinstance(value, str):
                        raise TypeError("str_field must be str")
                    self.str_field = value
                case "int_field":
                    if not isinstance(value, int):
                        raise TypeError("int_field must be int")
                    self.int_field = value
                case "list_field":
                    if not isinstance(value, list) or not all(
                        isinstance(n, str) for n in value
                    ):
                        raise TypeError("list_field must be list of str")
                    self.list_field = value
                case "dict_field":
                    if not isinstance(value, dict) or not all(
                        isinstance(n, str) for n in value.values()
                    ):
                        raise TypeError("dict_field must be dict of str")
                    self.dict_field = value
                case _:
                    raise ValueError(f"invalid argument: {key}")

    def deserialize(self, s: str) -> None:
        """deserialize json to data"""

        j = json.loads(s)
        self.set_fields(**j)

    def serialize(self) -> str:
        """serialize data to json"""

        return json.dumps(self.__dict__)


def main():
    """main entry point"""

    d1 = Data()
    d2 = Data(
        str_field="test",
        int_field=1,
        list_field=["list_test"],
        dict_field={"test_key": "test_value"},
    )

    s1 = d1.serialize()
    s2 = d2.serialize()
    d1.deserialize(s1)
    d2.deserialize(s2)

    print("s1:", s1)
    print("d1:", d1.__dict__)
    print("s2:", s2)
    print("d2:", d2.__dict__)


if __name__ == "__main__":
    main()
