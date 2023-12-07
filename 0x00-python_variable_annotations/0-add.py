#!/usr/bin/env python3
"""
file contains a type-annotated function add that takes a float (a)
and a float (b) as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns their sum.

    Parameters:
    - a (float): The first number.
    - b (float): The second number.

    Returns:
    float: The sum of the two numbers.
    """
    return a + b

    if __name__ == '__main__':
        print(add(1.11, 2.22) == 1.11 + 2.22)
        print(add.__annotations__)
