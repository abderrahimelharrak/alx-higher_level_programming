#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    x = sys.argv[1]

    t = requests.get(x)
    if t.status_code >= 400:
        print("Error code: {}".format(t.status_code))
    else:
        print(t.text)
