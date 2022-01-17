#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for e in my_list:
            if count >= x:
                raise
            count += 1
            print(e, end="")
    except Exception:
        pass
    finally:
        print()
    return count
