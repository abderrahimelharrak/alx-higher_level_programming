#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_liste = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            new_liste.append(True)
        else:
            new_liste.append(False)
    return new_liste
