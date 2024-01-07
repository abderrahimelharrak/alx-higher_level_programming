#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    x = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(x) as y:
        z = y.read()
        print("Body response:")
        print("\t- type: {}".format(type(z)))
        print("\t- content: {}".format(z))
        print("\t- utf8 content: {}".format(z.decode("utf-8")))
