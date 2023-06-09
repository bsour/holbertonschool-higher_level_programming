#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_numbers = list(set(my_list))
    total = sum(sorted_numbers)
    return total
