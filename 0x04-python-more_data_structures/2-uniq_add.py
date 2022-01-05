#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(list(map(lambda e: e, list(set(my_list)))))
