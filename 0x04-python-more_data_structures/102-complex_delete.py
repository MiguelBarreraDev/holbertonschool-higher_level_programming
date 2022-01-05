#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    save = a_dictionary.copy()
    for key in save.keys():
        if a_dictionary.get(key) == value:
            a_dictionary.pop(key)
    return a_dictionary
