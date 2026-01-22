#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?', and ':'

    Args:
        text: Text to format (must be string)

    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Initialize result
    result = ""
    i = 0
    
    # Process text character by character
    while i < len(text):
        result += text[i]
        
        # If we encounter punctuation
        if text[i] in ".?:":
            # Add two new lines
            result += "\n\n"
            
            # Skip any spaces after punctuation
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print the result without trailing spaces
    lines = result.split('\n')
    for line in lines:
        print(line.strip())
