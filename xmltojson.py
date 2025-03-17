import xmltodict
import json
import sys
from xml.etree import ElementTree as ET

def xml_to_json(xml_input, output_file=None):
    """
    Convert XML to JSON format.
    
    Args:
        xml_input (str): Either XML string or path to XML file
        output_file (str, optional): Path to save the output JSON file
    
    Returns:
        str: JSON string representation of the XML data
    """
    try:
        # Determine if input is a file path or XML string
        try:
            # First try to parse as file
            with open(xml_input, 'r', encoding='utf-8') as file:
                xml_content = file.read()
        except (FileNotFoundError, OSError):
            # If file not found, assume it's an XML string
            xml_content = xml_input

        # Parse XML string
        # First validate XML is well-formed
        ET.fromstring(xml_content)
        
        # Convert XML to dict
        xml_dict = xmltodict.parse(xml_content,
                                 process_namespaces=True,
                                 dict_constructor=dict)
        
        # Convert dict to JSON string
        json_output = json.dumps(xml_dict,
                               indent=2,
                               ensure_ascii=False)
        
        # If output file is specified, save to file
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(json_output)
        
        return json_output

    except ET.ParseError as e:
        return f"Error: Invalid XML format - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Command line interface
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python xml_to_json.py input.xml [output.json]")
        print("  OR")
        print("  python xml_to_json.py -s '<xml_string>' [output.json]")
        return

    # Check if input is string or file
    if sys.argv[1] == '-s':
        if len(sys.argv) < 3:
            print("Error: XML string must be provided after -s flag")
            return
        xml_input = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
    else:
        xml_input = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = xml_to_json(xml_input, output_file)
    
    # Print result if it's not an error message
    if not result.startswith("Error:"):
        print("Conversion successful!")
        print("\nJSON Output:")
        print(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
