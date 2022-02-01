#!/usr/bin/python3
""" Use the module for adds all argument to a Python list,
    and the save them to a file
"""
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []

try:
    with open("add_item.json", "r") as file:
        my_list = json.loads(file.read())
except FileNotFoundError:
    pass
finally:
    with open("add_item.json", "w") as file:
        for pos in range(1, len(sys.argv)):
            my_list.append(sys.argv[pos])
        file.write(json.dumps(my_list))
