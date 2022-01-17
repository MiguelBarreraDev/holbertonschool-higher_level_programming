#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    count = 0
    while pos < x:
        try:
            if type(my_list[pos]) is int:
                print("{:d}".format(my_list[pos]), end="")
                count += 1
        except IndexError:
            raise
        pos += 1
    print()
    return count
