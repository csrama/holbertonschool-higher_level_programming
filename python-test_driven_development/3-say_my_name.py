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
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print exactly as in the example
    # When last_name is empty, still print a space after first_name
    print("My name is {} {}".format(first_name, last_name))
