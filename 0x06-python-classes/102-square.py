#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Check if two Square instances have equal areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if two Square instances have different areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Check if the area of the current Squar

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if the area of the current Squar

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Check if the area of the current Square

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if the area of the current Square

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
