#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    liste_keys = list(a_dictionary.keys())

    for value_dictionnaire in liste_keys:
        if value == a_dictionary.get(value_dictionnaire):
            del a_dictionary[value_dictionnaire]

    return (a_dictionary)
