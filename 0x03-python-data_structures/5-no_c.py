#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    my_string = list(my_string)
    for c in my_string:
        if c == 'c' or c == 'C':
            my_string[idx] = ''
        idx += 1
    return "".join(my_string)
