#!/usr/bin/env python3

"""
Contains a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Parameters:
    - mxd_lst (List[Union[int, float]]): The input list of integers and floats.

    Returns:
    float: The sum of the input list.
    """
    return sum(mxd_lst)


if __name__ == '__main__':
    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(
        ans, type(ans))
        )
