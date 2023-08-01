from docx import Document
import re
import pandas as pd
import sys

def extract_abbreviations(docx_file):
    document = Document(docx_file)
    abbreviations = set()

    # Regular expression to match potential abbreviations
    abbreviation_pattern = r'\b[A-Z]{2,}\b'

    for paragraph in document.paragraphs:
        matches = re.findall(abbreviation_pattern, paragraph.text)
        abbreviations.update(matches)

    return abbreviations

def expand_abbreviation(abbreviation):
    # Replace this with your custom abbreviation expander logic
    # For example, you can define a dictionary of abbreviations and their corresponding full names.
    abbreviation_map = {
        "ABC": "American Broadcasting Company",
        "NASA": "National Aeronautics and Space Administration",
        # Add more mappings as needed
    }
    return abbreviation_map.get(abbreviation, abbreviation)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_abbreviations.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    abbreviations = extract_abbreviations(input_file)
    full_names = {abbr: expand_abbreviation(abbr) for abbr in abbreviations}

    # Print the sorted list of abbreviations
    print("Abbreviations:")
    for abbreviation in sorted(abbreviations):
        print(abbreviation)

    df = pd.DataFrame({"Abbreviation": list(full_names.keys()), "Full Name": list(full_names.values())})
    df.to_csv("abbreviations.csv", index=False)

    #print("CSV file generated successfully.")
