#!/usr/bin/python3
""" 0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """ giving n x n 2D matrix and rotating it 90 degrees clockwise
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ calling the rotate_2d_matrix(matrix) """
    rotate_2d_matrix(matrix)
    print(matrix)
