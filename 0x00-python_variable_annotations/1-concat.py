#!/usr/bin/env python3
"""
A type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Parameters:
    - str1 (str): The first string.
    - str2 (str): The second string.

    Returns:
    str: The concatenated string.
    """
    return str1 + str2

    if __name__ == "__main__":
        str1 = "egg"
        str2 = "shell"

        print(concat(str1, str2) == "{}{}".format(str1, str2))
        print(concat.__annotations__)
