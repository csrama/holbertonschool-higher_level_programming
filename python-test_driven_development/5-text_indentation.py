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

    # Process the text
    i = 0
    text_len = len(text)
    
    while i < text_len:
        # Print current character
        print(text[i], end="")
        
        # Check for punctuation
        if text[i] in ".?:":
            print("\n")
            
            # Skip spaces after punctuation
            i += 1
            while i < text_len and text[i] == ' ':
                i += 1
            continue
        
        i += 1
