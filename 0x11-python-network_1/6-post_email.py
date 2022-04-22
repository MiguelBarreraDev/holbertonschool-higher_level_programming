#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    [url, email] = argv[1:]

    send_values = {"email": email}
    res = requests.post(url, data=send_values)
    print(res.text)
