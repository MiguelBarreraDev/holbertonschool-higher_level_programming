#!/usr/bin/python3
""" Use the module for appends a string at the end of the text file

    Functions:
        append_write

"""


def append_write(filename="", text=""):
    """
        Args:
            filename(str): File path
            text(str): string to append
    """
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
