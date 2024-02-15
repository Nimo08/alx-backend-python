#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and
apply any necessary changes.
"""


import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> \
                typing.List[typing.Any]:
    """
    Takes a tuple 'lst' and an integer 'factor' and returns
    a list containing each element of the tuple duplicated
    'factor' times.
    """
    zoomed_in: typing.List[typing.Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

array_tuple = tuple(array)
zoom_2x = zoom_array(array_tuple)

zoom_3x = zoom_array(array_tuple, 3)
