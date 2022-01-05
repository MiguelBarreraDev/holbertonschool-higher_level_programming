#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda e: replace if e == search else e, my_list))
    return new_list
