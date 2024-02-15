#!/usr/bin/env python3
"""
Type-annotated function: make_multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    Result function: multiplies a float by multiplier.
    """
    def result(num: float) -> float:
        return num * multiplier
    return result
