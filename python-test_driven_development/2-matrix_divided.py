#!/usr/bin/python3
"""
Module for dividing all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers or floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with all elements divided by div, rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Error messages
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"
    
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    
    # Check if matrix is not empty
    if not matrix:
        raise TypeError(matrix_error)
    
    # Check if each element in matrix is a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_error)
    
    # Check if matrix has at least one row and it's not empty
    if not matrix[0]:
        raise TypeError(matrix_error)
    
    # Check if all rows have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(size_error)
    
    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_error)
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Handle division by infinity
    if div == float('inf') or div == float('-inf'):
        # Any number divided by infinity is 0
        return [[0.0 for _ in row] for row in matrix]
    
    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Divide and round to 2 decimal places
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
