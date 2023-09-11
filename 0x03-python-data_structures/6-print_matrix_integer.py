#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for c in l:
            print("{:d}".format(c), end=" " if c != l[-1] else "")
        print()
