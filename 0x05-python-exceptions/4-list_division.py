#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    pos = 0
    while pos < list_length:
        try:
            result = my_list_1[pos] / my_list_2[pos]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        except BaseException:
            result = 0
            print("wrong type")
        finally:
            new_list.append(result)
        pos += 1
    return new_list
