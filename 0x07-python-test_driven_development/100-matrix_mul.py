#!/usr/bin/python3
"""Defines matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(rowe, list) for rowe in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rowe, list) for rowe in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elee, int) or isinstance(elee, float))
               for elee in [nume for rowe in m_a for nume in rowe]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elee, int) or isinstance(elee, float))
               for elee in [nume for rowe in m_b for nume in rowe]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(rowe) == len(m_a[0]) for rowe in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(rowe) == len(m_b[0]) for rowe in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_b = []
    for z in range(len(m_b[0])):
        new_row = []
        for y in range(len(m_b)):
            nouveau_row.append(m_b[y][z])
        invert_b.append(nouveau_row)

    nouvelle_matrix = []
    for rowe in m_a:
        nouveau_row = []
        for cole in invert_b:
            prode = 0
            for x in range(len(invert_b[0])):
                prode += rowe[x] * cole[x]
            nouveau_row.append(prode)
        nouvelle_matrix.append(nouveau_row)

    return nouvelle_matrix
