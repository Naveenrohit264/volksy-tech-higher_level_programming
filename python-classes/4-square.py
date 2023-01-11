#!/usr/bin/python3
"""creating class """


class Square:
    """clas for square"""
    def __init__(self, size=0):
        """initialize data"""
        self.__size = size
    def area(self)i:
        """return square area"""
        return(self.__size ** 2)
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
