#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    data = {
        "q": "" if len(argv) < 2 else argv[1]
    }

    res = requests.post(url, data=data)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except Exception:
        print("Not a valid JSON")
