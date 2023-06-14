#!/usr/bin/python3

"""
Define a Square class.
"""


class Square:
    """
    Represent a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError("must be a tuple of 2 pos integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Print the square.

        If size is 0, print an empty line.
        the position by printing spaces before each line if position[1] > 0.
        """
        if self.size == 0:
            print("")
        for row in range(self.size):
            if row == 0:
                for i in range(self.position[1]):
                    print("")
            if self.position[0] > 0:
                for j in range(self.position[0]):
                    print("_", end="")
            for col in range(self.size):
                print("#", end="")
            print("")
