#!/usr/bin/python3
"""
This module defines a Square class.
"""
class Square:

    def __init__(self, size=0):
        """
        this initalises the class with size attribute ,thus validate the input
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        this calculates the area of the square
        """
        return self.__size**2
