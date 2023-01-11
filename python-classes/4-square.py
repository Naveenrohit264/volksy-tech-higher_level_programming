#!/usr/bin/python3
"""creating a class"""

class Square:
    """creating class for square"""

    
    def __init__(self, size=0):
        """Initializing data"""
        self.__size = size

    def area(self):
        """return area of square"""
    return(self.__size ** 2)
    
    @property
    def size(self):
        """retrieve size"""
        return(self.__size)
   
    @size.setter
    def size(self, value):
        """set size and handle error"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value