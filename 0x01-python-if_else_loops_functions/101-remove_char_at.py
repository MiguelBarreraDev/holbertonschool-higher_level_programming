#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and len(str) > n:
        str = str.replace(str[n], "")
    return str
