#!/usr/bin/python3
""" Use the module for reads stdin line by line and computers metrics
"""

import sys

lim = 0
arr = []
try:
    for line in sys.stdin:
        arr.append(list(filter(lambda e: e != "-", line.split(" "))))
        arr[lim] = arr[lim][-2:]
        lim += 1
        if lim == 10:
            break
except KeyboardInterrupt:
    pass

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

for line in arr:
    if line[0] in metrics["status"].keys():
        metrics["status"][line[0]] += 1

    metrics["size"] += int(line[1].replace("\n", ""))

print("File size {:d}".format(metrics["size"]))
for status in metrics["status"].keys():
    if metrics["status"][status] != 0:
        print("{}: {:d}".format(status, metrics["status"][status]), flush=True)
