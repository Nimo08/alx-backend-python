#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types.
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                    typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Takes an iterable containing sequences i.e. list or tuple and
    returns a list of tuples containing a sequence type and an integer.
    """
    return [(i, len(i)) for i in lst]
