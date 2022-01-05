#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    convert = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if type(roman_string) != str or roman_string is None:
        return 0
    if roman_string.count('I') > 3:
        return 0
    for key in roman_string:
        if key in convert.keys():
            number += convert.get(key)
    return number
