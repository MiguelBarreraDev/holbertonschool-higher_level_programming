#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    pos = 0;
    curr = 0
    after = 0
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

    lg = len(roman_string)
    for key in roman_string:
        curr = convert.get(key)
        after = convert.get(roman_string[pos + 1]) if pos + 1 < lg else 0
        if key in convert.keys():
            number += convert.get(key)
        pos += 1
    return number
