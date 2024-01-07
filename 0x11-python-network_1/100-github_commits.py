#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    x = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    t = requests.get(x)
    com = t.json()
    try:
        for z in range(10):
            print("{}: {}".format(
                com[z].get("sha"),
                com[z].get("commit").get("author").get("name")))
    except IndexError:
        pass
