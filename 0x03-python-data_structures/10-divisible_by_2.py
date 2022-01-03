#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    val_list = []

    for e in my_list:
        if e % 2 == 0:
            val_list.append(True)
        else:
            val_list.append(False)
    return val_list
