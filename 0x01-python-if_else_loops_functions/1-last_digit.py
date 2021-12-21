#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
lastDigit = (lastDigit - 10) if (number < 0) else lastDigit
fragment = "Last digit of {:d} is {:d} and is "
if lastDigit > 5:
    print(fragment.format(number, lastDigit) + "greater than 5")
elif lastDigit == 0:
    print(fragment.format(number, lastDigit) + "0")
else:
    print(fragment.format(number, lastDigit) + "less than 6 and not 0")
