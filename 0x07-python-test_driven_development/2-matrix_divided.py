#!/usr/bin/python3
""" Split all elements of an array

    function:
        matrix_divided
"""


def matrix_divided(matrix, div):
    """ Definition of the function that will divide the elements of an array

        Args:
            param1 (list): list of lists of integers or floats
            param2 (int or float): can't be equal to 0

        Returns:
            list: list of lists
    """
    msg_TE1 = 'matrix must be a matrix (list of lists) of integers/floats'
    msg_TE2 = 'Each row of the matrix must have the same size'
    for row in matrix:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError(msg_TE)

    len_row = list(map(lambda row: len(row), matrix))
    set_row = set(len_row)
    if matrix != [] and len(set_row) != 1:
        raise TypeError(msg_TE2)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(
        lambda row: list(map(
            lambda e: round(e / div, 2),
            row)),
        matrix)
                )
