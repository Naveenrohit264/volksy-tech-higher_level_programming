#!/usr/bin/python3
""" function to returns the list of available attributes and methods of an object"""


def lookup(obj):
        """returns the list of available attributes and methods of an object"""
        return dir(obj)
