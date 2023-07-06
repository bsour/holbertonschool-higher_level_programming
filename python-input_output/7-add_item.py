#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.

Usage: ./7-add_item.py [args]

"""

import sys
from os import path
from json import dump, load

filename = "add_item.json"

if path.isfile(filename):
    with open(filename, 'r') as file:
        items = load(file)
else:
    items = []

items.extend(sys.argv[1:])

with open(filename, 'w') as file:
    dump(items, file)
