#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == '__main__':
    match = {'+': add, '-': sub, '*': mul, '/': div}
    argv = sys.argv
    lenArg = len(argv)
    # start - validate argument number
    if lenArg != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)
    # end - validate argument number

    op = argv[2]
    # start - Validate operator
    val = 0
    for op_list in ['+', '-', '*', '/']:
        if op_list == op:
            val += 1
    if val == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    # end - validate operator

    a = int(argv[1])
    b = int(argv[3])

    print("{:d} {} {:d} = {:d}".format(a, op, b, match[op](a, b)))
    sys.exit(0)
