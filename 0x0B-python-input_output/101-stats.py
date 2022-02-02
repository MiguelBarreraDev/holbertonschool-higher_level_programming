#!/usr/bin/python3
""" Use the module for reads stdin line by line and computers metrics
"""


import sys


lim = 0
arr = []
metrics = {
    "size": 0,
    "status": {
        "200": 0,
        "301": 0,
        "400": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
}
try:
    """Get Data(status_code, size)"""
    for line in sys.stdin:
        arr.append(line.split())
        arr[lim] = arr[lim][-2:]

        metrics["size"] += int(arr[lim][-1].replace("\n", ""))

        lim += 1

        if lim % 10 == 0:
            """Count status_code"""
            for line in arr:
                if line[0] in metrics["status"].keys():
                    metrics["status"][line[0]] += 1

            """Output format"""
            print("File size: {:d}".format(metrics["size"]))
            for status in metrics["status"].keys():
                if metrics["status"][status] != 0:
                    print("{}: {:d}".format(status, metrics["status"][status]))

    """Output format"""
    print("File size: {:d}".format(metrics["size"]))
    for status in metrics["status"].keys():
        if metrics["status"][status] != 0:
            print("{}: {:d}".format(status, metrics["status"][status]))
except KeyboardInterrupt:
    print("File size: {:d}".format(metrics["size"]))
    for status in metrics["status"].keys():
        if metrics["status"][status] != 0:
            print("{}: {:d}".format(status, metrics["status"][status]))
    raise
