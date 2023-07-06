#!/usr/bin/python3
"""
    3-write_file.py
    Function that writes a string to a text file\
    (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Reads n lines of a text file (UTF8) and prints it to stdout."""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
