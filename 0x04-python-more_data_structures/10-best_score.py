#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_values = sorted(a_dictionary.values(), reverse=True)
        for key in a_dictionary.keys():
            if a_dictionary[key] == list_values[0]:
                return key
