#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    x = sys.argv[1]

    y = requests.get(x)
    print(y.headers.get("X-Request-Id"))
