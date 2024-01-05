#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    s = len(list_of_integers)
    m_e = s
    m = s // 2

    if s == 0:
        return None

    while True:
        m_e = m_e // 2
        if (m < s - 1 and
                list_of_integers[m] < list_of_integers[m + 1]):
            if m_e // 2 == 0:
                m_e = 2
            m = m + m_e // 2
        elif m_e > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            if m_e // 2 == 0:
                m_e = 2
            m = m - m_e // 2
        else:
            return list_of_integers[m]
