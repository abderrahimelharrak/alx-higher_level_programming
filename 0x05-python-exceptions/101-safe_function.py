#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        m = fct(*args)
    except Exception as e:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
    else:
        return m
