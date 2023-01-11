#!/usr/bin/python3
"""creating class """


class Square:
    """clas for square"""
    def __init__(self, size=0):
        """initialize data"""
        size.__size = size
    def area(self):
        """return square area"""
        return(self.__size ** size)
    def size(self):
        """retrive size"""
        return(self.__size)
    def size(self,value):
        """handling errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value
