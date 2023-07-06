#!/usr/bin/python3
"""
    6-from_json_string.py
    Function that writes an Object to \
    a text file, using a JSON representation.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(obj):
        """Function that writes an Object to \
        a text file, using a JSON representation."""
        return obj.__dict__
