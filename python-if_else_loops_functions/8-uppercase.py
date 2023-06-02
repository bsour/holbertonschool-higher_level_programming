#!/usr/bin/env python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
            uppercase_str += uppercase_char
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
