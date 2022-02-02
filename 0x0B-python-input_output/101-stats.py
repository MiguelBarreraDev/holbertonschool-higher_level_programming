#!/usr/bin/python3
""" Use the module for reads stdin line by line and computers metrics
"""


import sys

size = 0
lim = 0
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
try:
    """Get Data(status_code, size)"""
    for line in sys.stdin:
        line = line.split()

        size += int(line[-1])

        lim += 1

        """Count status_code"""
        code = line[-2]
        if code in status.keys():
            status[code] += 1

        if lim % 10 == 0:
            """Output format"""
            print("File size: {:d}".format(size))
            for code in sorted(status.keys()):
                if status[code] != 0:
                    print("{}: {:d}".format(code, status[code]))

    """Output format"""
    print("File size: {:d}".format(size))
    for code in sorted(status.keys()):
        if status[code] != 0:
            print("{}: {:d}".format(code, status[code]))
except KeyboardInterrupt:
    """Output format"""
    print("File size: {:d}".format(size))
    for code in sorted(status.keys()):
        if status[code] != 0:
            print("{}: {:d}".format(code, status[code]))
