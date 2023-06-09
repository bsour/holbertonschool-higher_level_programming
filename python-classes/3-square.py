#!/usr/bin/python3

"""
Define a class Square.

This class represents a square and provides methods for size manipulation.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Init Square instance with a given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
