#!/usr/bin/python3
"""Defining a Pascal's Triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returning a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trie = triangle[-1]
        tmpe = [1]
        for i in range(len(trie) - 1):
            temp.append(trie[i] + trie[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangle
