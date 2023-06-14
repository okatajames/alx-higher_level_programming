#!/usr/bin/python3

"""A function that adds tuples and returns their sum"""


ddef add_tuple(tuple_a=(), tuple_b=()):
    at1, at2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    bt1, bt2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    result = (at1 + bt1, at2 + bt2)
    return (result)
