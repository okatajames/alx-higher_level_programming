#!/usr/bin/python3

"""A function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for k in range(len(matrix[index])):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(matrix[index][k]), end='')
        print()
