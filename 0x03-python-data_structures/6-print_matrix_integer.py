#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            print("{:d}".format(matrix[i][j]), end="")
            if j < columns - 1:
                print("", end=" ")
        print("")
