#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_arr = []
    for rows in matrix:
        new_arr.append(list(map(lambda e: e**2, rows)))
    return new_arr
