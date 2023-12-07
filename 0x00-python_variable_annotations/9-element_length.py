#!/usr/bin/env python3

"""
function that uses Duck typing
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of strings and returns a list of tuples.
    Each tuple contains a string from the input list and its length.

    Parameters:
    - lst (List[str]): The input list of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples where each tuple contains a string
    from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == '__main__':
    print(element_length.__annotations__)
