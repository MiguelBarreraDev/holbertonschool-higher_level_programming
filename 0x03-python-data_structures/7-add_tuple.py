#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = int
    second = int
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        if len(tuple_b) > 0:
            first = tuple_a[0] + tuple_b[0]
            second = tuple_a[1] + 0
        else:
            first = tuple_a[0]
            second = tuple_a[1]
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        if len(tuple_a) > 0:
            first = tuple_a[0] + tuple_b[0]
            second = 0 + tuple_b[1]
        else:
            first = tuple_b[0]
            second = tuple_b[1]

    return (first, second)
