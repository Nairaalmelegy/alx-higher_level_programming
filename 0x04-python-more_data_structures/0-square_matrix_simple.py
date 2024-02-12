#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    return [[y ** 2 for y in x] for x in matrix]
