#!/usr/bin/python3
"""0x0B-python-input_output Module"""


def pascal_triangle(n):
    """Returns Pascal's triangle up to the nth row."""
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle
