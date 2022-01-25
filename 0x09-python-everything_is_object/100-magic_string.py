#!/usr/bin/python3
def magic_string():
    magic_string.count = 1 if "count" not in magic_string.__dict__ else  magic_string.count + 1
    return "BestSchool" if magic_string.count == 1 else "BestSchool" + (", BestSchool" * magic_string.count)
