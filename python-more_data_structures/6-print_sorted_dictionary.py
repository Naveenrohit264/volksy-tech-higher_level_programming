#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedby = sorted(a_dictionary.item(), key = lambda t: t[0])
    return sortedby
