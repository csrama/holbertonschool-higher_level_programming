#!/usr/bin/python3
"""
Module for printing name
"""


def say_my_name(first_name, last_name=""):
    """
    Print 'My name is <first_name> <last_name>'

    Args:
        first_name: First name string
        last_name: Last name string (optional)

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    # Check if first_name is a string
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    # Print the formatted name
    print(f"My name is {first_name} {last_name}".rstrip())



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
