#!/usr/bin/python3
"""
    6-from_json_string.py
    Function that writes an Object to \
    a text file, using a JSON representation.
"""
import json


def load_from_json_file(filename):
    """Function that writes an Object to \
    a text file, using a JSON representation."""
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
