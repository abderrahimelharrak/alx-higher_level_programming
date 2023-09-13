#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    liste_keys = list(a_dictionary.keys())

    for x in liste_keys:
        number += 1

    return (number)
