#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    liste_ordered = list(a_dictionary.keys())
    liste_ordered.sort()
    for x in liste_ordered:
        print("{}: {}".format(x, a_dictionary.get(x)))
