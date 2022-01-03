#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for e in reversed(my_list):
        print("{:d}".format(e))

my_list = []
print_reversed_list_integer(my_list)
