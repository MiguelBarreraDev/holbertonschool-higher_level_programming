#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    lenArg = len(argv) - 1
    pos = 0
    if lenArg == 0:
        print("{:d} arguments.".format(lenArg))
    elif lenArg == 1:
        print("{:d} argument:".format(lenArg))
        for i in argv:
            if pos != 0:
                print("{:d}: {}".format(pos, i))
            pos += 1
    else:
        print("{:d} arguments:".format(lenArg))
        for i in argv:
            if pos != 0:
                print("{:d}: {}".format(pos, i))
            pos += 1
