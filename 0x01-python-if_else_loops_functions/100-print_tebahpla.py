#!/usr/bin/python3
for alpha in reversed(range(65, 91)):
    print("{:c}".format((alpha + 32) if (alpha % 2 == 0) else alpha), end="")
