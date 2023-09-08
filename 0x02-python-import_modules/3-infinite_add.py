#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    totale = 0
    for x in range(len(sys.argv) - 1):
        totale += int(sys.argv[x + 1])
    print("{}".format(totale))
