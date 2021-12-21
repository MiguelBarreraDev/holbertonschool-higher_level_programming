#!/usr/bin/python3
for fDigit in range(10):
    if fDigit == 8:
        break
    for sDigit in range(fDigit + 1, 10):
        print("{:d}{:d}".format(fDigit, sDigit), end=", ")
print("89")
