#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":

    import urllib.request
    from sys import argv

    url = argv[1]
    key = "X-Request-Id"

    with urllib.request.urlopen(url) as res:
        print(dict(res.headers._headers).get(key))
