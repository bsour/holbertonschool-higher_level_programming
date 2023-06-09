#!/usr/bin/python3
"""
Function to replace some characters with '\n\n'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after some characters.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    tmp = text.replace(".", ".\n\n")
    tmp = tmp.replace(":", ":\n\n")
    tmp = tmp.replace("?", "?\n\n")
    p = tmp.splitlines(True)
    ls_strip = []
    for line in p:
        if line == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(line.lstrip())
    print("".join(ls_strip), end="")
