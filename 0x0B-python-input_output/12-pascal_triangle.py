#!/usr/bin/python3
""" Use the module for get list of lists of integers
    representing

    Function:
        pascal_triangle
"""


def pascal_triangle(n):
    """ Function definition
        Args:
            n(int): Number of levels of Pascal's triangle
    """
    dlist = []
    if n <= 0:
        return dlist
    dlist.append([1])
    for row in range(1, n):
        dlist.append([])
        for i in range(len(dlist[row - 1]) + 1):
            if i == 0 or i == len(dlist[row - 1]):
                dlist[row].append(1)
            else:
                dlist[row].append(dlist[row - 1][i] + dlist[row - 1][i - 1])
    return dlist
