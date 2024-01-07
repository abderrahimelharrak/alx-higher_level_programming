#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    x = sys.argv[1]

    y = urllib.request.Request(x)
    with urllib.request.urlopen(y) as z:
        print(dict(z.headers).get("X-Request-Id"))
