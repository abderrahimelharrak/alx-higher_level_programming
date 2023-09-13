#!/usr/bin/python3
def to_subtract(list_number):
    too_sub = 0
    max_liste = max(list_number)

    for x in list_number:
        if max_liste > x:
            too_sub += x

    return (max_liste - too_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    liste_keys = list(roman_n.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for x in roman_string:
        for r_number in liste_keys:
            if r_number == x:
                if roman_n.get(x) <= last_roman:
                    number += to_subtract(list_number)
                    list_number = [roman_n.get(x)]
                else:
                    list_number.append(roman_n.get(x))

                last_roman = roman_n.get(x)

    number += to_subtract(list_number)

    return (number)
