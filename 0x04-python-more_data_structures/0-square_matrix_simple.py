#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nouvelle_matrix = matrix.copy()

    for j in range(len(matrix)):
        nouvelle_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (nouvelle_matrix)
