#!/usr/bin/python3

""" Define class square with optional instantiation: size """


class Square:
    """
    A class that represents a square.

    Attributes:
    __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square instance with a given size.
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
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
