#!/usr/bin/python3
for pos in range(26):
    print(chr(122 - pos - 32) if (pos % 2 != 0) else (chr(122 - pos)), end="")
