#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for e in sorted(a_dictionary.items()):
        print("{}: {}".format(e[0], e[1]))
