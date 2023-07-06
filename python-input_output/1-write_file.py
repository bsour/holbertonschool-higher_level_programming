#!/usr/bin/python3
"""
    1-number_of_lines
    Returns the number of lines of a text file.
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file."""
    with open(filename, encoding='utf-8') as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
