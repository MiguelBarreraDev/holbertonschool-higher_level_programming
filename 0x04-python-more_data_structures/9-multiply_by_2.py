#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list_of_tuples = a_dictionary.items()
    new_dictionary = {}
    for tpl in list_of_tuples:
        new_dictionary.update({tpl[0]: (tpl[1] * 2)})
    return new_dictionary
