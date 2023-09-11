#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nouvelle_tuple = ()
    tuple_un = tuple_a + (0, 0)
    tuple_deux = tuple_b + (0, 0)
    nouvelle_tuple = tuple_un[0] + tuple_deux[0], tuple_un[1] + tuple_deux[1]
    return nouvelle_tuple
