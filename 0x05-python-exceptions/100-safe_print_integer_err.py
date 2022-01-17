#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as mesg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return False
    return True
