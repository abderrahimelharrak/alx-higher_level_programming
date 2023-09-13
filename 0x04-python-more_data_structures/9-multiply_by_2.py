#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionnaire = a_dictionary.copy()
    liste_keys = list(new_dictionnaire.keys())

    for x in liste_keys:
        new_dictionnaire[x] *= 2

    return (new_dictionnaire)
