#!/usr/bin/python3
"""creating a class"""

class Square:
    """creating class for square"""
    def __init__(self, size=0):
        """constructor"""
        self.__size = size

    def area(self):
        """area of square"""
        return(self.__size * self.__size)

    def size(self):
        """size private"""
        self.__size = size

    def size(self, value):
        """validation"""
        if type(value) is not int:
            return TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
