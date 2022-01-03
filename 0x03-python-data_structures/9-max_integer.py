#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_e = my_list[0]
    for e in my_list:
        if e > max_e:
            max_e = e
    return max_e
