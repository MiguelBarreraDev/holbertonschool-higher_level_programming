#!/usr/bin/python3
def no_c(my_string):
    chrs = "cC"
    for c in chrs:
        my_string = my_string.replace(c, '')
    return my_string
