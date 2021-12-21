#!/usr/bin/python3
def uppercase(str):
    for pos in str:
        pos = ord(pos)
        pos = (pos - 32) if (pos >= 97 and pos <= 122) else (pos)
        print("{}".format(chr(pos)), end="")
    print("")
