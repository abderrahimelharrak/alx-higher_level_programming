#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    dem = 0

    for tupp in my_list:
        number += tupp[0] * tupp[1]
        dem += tupp[1]

    return (number / dem)
