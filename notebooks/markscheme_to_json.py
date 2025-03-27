import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    """
    Reads a CSV file and converts it into a JSON file.

    Args:
        csv_file_path (str): The path to the input CSV file.
        json_file_path (str): The path to the output JSON file.
    """
    data = []

    with open(csv_file_path, 'r') as csvfile:
        crit_csv = csv.DictReader(csvfile)
    
        for row in crit_csv:
            data.append(row)

    json_docs = {'name': 'markscheme_ks2',
            'description': 'ks2 marking criteria codes and usage',
            'data': data
            }

    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_docs, jsonfile, indent=4) 
    
    print(f"CSV data successfully converted to JSON and saved to {json_file_path}")

# Example usage:
csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "markscheme_KS2_labelled.csv") 
json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "markscheme_KS2_labelled.json") 

csv_to_json(csv_file, json_file)