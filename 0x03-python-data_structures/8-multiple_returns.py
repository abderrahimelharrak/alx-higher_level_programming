#!/usr/bin/python3
def multiple_returns(sentence):
    ma_tuple = ()
    if len(sentence) == 0:
        ma_tuple = 0, "None"
    else:
        ma_tuple = len(sentence), sentence[0]
    return ma_tuple
