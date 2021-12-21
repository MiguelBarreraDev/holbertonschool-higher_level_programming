#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = number % 10
    lastDigit = (10 - lastDigit) if (number < 0) else (lastDigit)
    print(lastDigit, end="")
    return lastDigit
