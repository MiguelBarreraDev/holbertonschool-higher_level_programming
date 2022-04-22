#!/usr/bin/python3
"""
Uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url_api = "https://api.github.com/user"

    res = requests.get(url_api, auth=(argv[1], argv[2]))
    res = res.json()
    print(res.get("id"))
