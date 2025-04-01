import csv
import json
from pathlib import Path

def csv_to_json(csv_file_path, json_file_path=None, indent=4):
    """
    Converts a CSV file to JSON format.
    
    Args:
        csv_file_path (str): Path to the input CSV file
        json_file_path (str): Path to save the output JSON file (optional)
        indent (int): Indentation level for pretty-printed JSON (None for compact)
    
    Returns:
        dict: The converted JSON data if json_file_path is None
        str: Path to the saved JSON file if json_file_path is provided
    """
    try:
        # Read CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Handle output
        if json_file_path is None:
            return data
        else:
            with open(json_file_path, mode='w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=indent, ensure_ascii=False)
            return json_file_path
    
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Configuration - set these values directly
    input_csv = "data.csv"          # Path to your input CSV file
    output_json = "data.json"       # Path for output JSON file (None to return dict)
    json_indent = 4                 # Indentation for pretty JSON (None for compact)
    
    # Convert CSV to JSON
    result = csv_to_json(input_csv, output_json, json_indent)
    
    # Print status
    if result is None:
        print("Conversion failed.")
    elif isinstance(result, str):
        print(f"Successfully converted CSV to JSON: {result}")
    else:
        print("CSV converted to JSON data:")
        print(json.dumps(result, indent=json_indent, ensure_ascii=False))