#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): A matrix represented as a list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the divided elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a non-empty list of lists of integers/floats,
                   if the rows of the matrix do not have the same size, or
                   if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix_divided([[1, 2], [3, 4], [5, 6]], 3)
        [[0.33, 0.67], [1.0, 1.33], [1.67, 2.0]]

    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a non-empty list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
