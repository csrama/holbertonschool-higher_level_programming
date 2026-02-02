#!/usr/bin/env python3
"""
Task 2: Converting CSV Data to JSON Format
Convert CSV data to JSON format using serialization techniques.
"""

import csv
import json
import os


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert a CSV file to JSON format.
    
    Args:
        csv_filename (str): The name/path of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Check if file exists
        if not os.path.exists(csv_filename):
            return False
        
        # Read CSV data
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                data.append(row)
        
        # Write JSON data
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        
        return True
        
    except Exception:
        return False
