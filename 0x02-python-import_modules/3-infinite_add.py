#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    lenArg = len(argv)
    pos = 0
    sumando = 0
    if lenArg == 1:
        sumando = 0
    else:
        for i in argv:
            if pos != 0:
                sumando += int(i)
            pos += 1
    print(sumando)
