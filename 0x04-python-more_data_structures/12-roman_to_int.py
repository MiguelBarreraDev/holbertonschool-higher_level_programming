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
    pos = 0
    current = 0
    after = 0
    len_roman = len(roman_string)
    if type(roman_string) != str or roman_string is None:
        return 0
    if roman_string.count('I' > 4):
        return 0
    for letter in roman_string:
        current = convert.get(letter)
        after = convert[roman_string[pos + 1]] if pos + 1 < len_roman else 0
        if after > current:
            number += after - current
            break
        number += convert[letter]
        pos += 1
    return number
