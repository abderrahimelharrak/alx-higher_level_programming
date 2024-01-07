#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    x = sys.argv[1]
    y = {"email": sys.argv[2]}
    z = urllib.parse.urlencode(y).encode("ascii")

    rq = urllib.request.Request(x, z)
    with urllib.request.urlopen(rq) as res:
        print(res.read().decode("utf-8"))
