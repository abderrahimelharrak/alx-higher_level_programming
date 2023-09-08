#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
    for x in range(counter):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
