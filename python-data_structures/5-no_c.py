#!/usr/bin/python3
def no_c(my_string):
    replacements = [('c', ''), ('C', '')]
    for char, replacement in replacements:
        if char in my_string:
            my_string = my_string.replace(char, replacement)
    return my_string
