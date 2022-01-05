#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set(list(filter(lambda e: (e in set_1) and (e in set_2), set_1)))
    return new_set
