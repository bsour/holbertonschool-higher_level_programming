#!/usr/bin/python3

"""Define a class square.
This class represents a square and its private attribute
"""

class Square:
    """
    Class representing square.

    Attributes:
    __size: The size of the square.
    """
    def __init__(self, size):
        """
        Inititalises a square instance.

        Args:
        size (int): The size of the square.
        """
        self.__size = size
