#!/usr/bin/python3
""" Use the module for inser line in a text file

    Functions:
        append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function definition
    """
    arr_lines = []
    with open(filename, "r", encoding="UTF-8") as file:
        line = file.readline()
        arr_lines.append(line)
        while line:
            if search_string in line:
                arr_lines.append(new_string)
            line = file.readline()
            arr_lines.append(line)

    with open(filename, "w") as file:
        file.write("".join(arr_lines))
