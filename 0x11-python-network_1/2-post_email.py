#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    [url, email] = argv[1:]
    params = {"email": email}
    data = urllib.parse.urlencode(params)
    data = data.encode("ascii")  # Data should be bytes
    req = urllib.request.Request(url, data)

    # With data argument the request will use POST method
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
