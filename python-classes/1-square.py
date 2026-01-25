#!/usr/bin/python3
"""
Square module
Defines a Square class with private size attribute
"""


class Square:
    """
    Square class
    Defines a square with private size attribute
    """
    
    def __init__(self, size):
        """
        Initialize a new Square
        
        Args:
            size: Size of the square
        """
        self.__size = size
