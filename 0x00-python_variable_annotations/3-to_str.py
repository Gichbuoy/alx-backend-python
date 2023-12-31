#!/usr/bin/env python3
"""
type-annotated function to_str that takes a float n as argument
and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to its string representation.

    Parameters:
    - n (float): The input floating-point number.

    Returns:
    str: The string representation of the input number.
    """
    return str(n)

    if __name__ == '__main__':
        pi_str = to_str(3.14)
        print(pi_str == str(3.14))
        print(to_str.__annotations__)
        print("to_str(3.14) returns {} which is a {}".format(
            pi_str, type(pi_str)))
