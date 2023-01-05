#!/usr/bin/python3
def max_integer(my_list):
    if len(my_list) < 1:
        return None
    higher = 0
    for i in my_list:
        if i > higher:
            higher = i
    return 
