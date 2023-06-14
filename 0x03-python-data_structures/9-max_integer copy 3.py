#!/usr/bin/python3

"""A func that returns the max value in a list"""


def max_integer(my_list=[]):
    my_list.sort(reverse=True)
    max_int = my_list[0]
    return (max_int)
