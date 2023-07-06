#!/usr/bin/python3
"""
    2-read_lines.py
    Reads n lines of a text file (UTF8) and prints it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout."""
    n_lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            n_lines += 1

    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines >= n_lines:
            print(f.read(), end="")

        n_lines = 0
        for line in f:
            n_lines += 1
            if n_lines <= nb_lines:
                print(line, end="")
                continue
            break
