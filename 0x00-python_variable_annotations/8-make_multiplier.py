#!/usr/bin/env python3

"""
function that contains a type-annotated function make_multiplier that takes
a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Parameters:
    - multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies its argument by
    the specified multiplier.
    """
    def inner(value: float) -> float:
        """Returns a float multiplied by itself"""
        return multiplier * value
    return inner


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
