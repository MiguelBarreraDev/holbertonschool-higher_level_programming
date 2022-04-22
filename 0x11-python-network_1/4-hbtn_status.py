#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    url = "https://intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
