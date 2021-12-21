#!/usr/bin/python3
for pos in range(26):
    pos = 122 - pos
    letter = chr(pos - 32) if (pos % 2 != 0) else (chr(pos))
    print(letter, end="")
