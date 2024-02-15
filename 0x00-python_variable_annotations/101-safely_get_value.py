#!/usr/bin/env python3
"""
Given the parameters and the return values
add type annotations to the function.
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, None] = None) -> \
                        typing.Union[typing.Any, T]:
    """
    Takes a dictionary, its key and a default value of type 'T' or NoneType and
    returns either a value associated with the key in dct or default value
    if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
