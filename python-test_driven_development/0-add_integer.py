#!/usr/bin/python3
"""A function that adds two integers"""


def add_integer(a, b=98):
    """
    Return the sum of two integers

    Parameters:
        a: first integer
        b: second integer

    Returns: a + b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
