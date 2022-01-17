from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        stderr.write(str(err))
        return False
    return True
