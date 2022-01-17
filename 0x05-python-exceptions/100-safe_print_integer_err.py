#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write(str(err))
        return False
    return True
