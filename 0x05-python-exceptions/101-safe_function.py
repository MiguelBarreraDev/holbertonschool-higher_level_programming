#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return None
