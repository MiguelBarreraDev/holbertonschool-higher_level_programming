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
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
try:
    """Get Data(status_code, size)"""
    for line in sys.stdin:
        line = line.split()

        try:
            size += int(line[-1])
        except BaseException:
            pass

        try:
            """Count status_code"""
            code = line[-2]
            if code in list(status.keys()):
                status[code] += 1
        except BaseException:
            pass

        lim += 1

        if lim % 10 == 0:
            """Output format"""
            print("File size: {:d}".format(size))
            for key in sorted(status.keys()):
                if status[key] != 0:
                    print("{}: {:d}".format(key, status[key]))

    """Output format"""
    print("File size: {:d}".format(size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {:d}".format(key, status[key]))
except KeyboardInterrupt:
    """Output format"""
    print("File size: {:d}".format(size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {:d}".format(key, status[key]))
