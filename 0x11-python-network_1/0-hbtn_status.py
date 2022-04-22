#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as res:
    body = res.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
