#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for e in my_list:
        if e != my_list[idx]:
            new_list.append(e)
    my_list = new_list
    return new_list
