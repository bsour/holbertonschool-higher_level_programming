#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, val in enumerate(row):
            print("{:d}".format(val), end="")
            if index < len(row) - 1:
                print(" ", end="")
        print()
