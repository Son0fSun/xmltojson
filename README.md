# XML to JSON Converter

A Python script for converting XML files or strings to JSON format, preserving the structure and attributes of the original XML.

## Features

- Converts XML files or strings to JSON format
- Preserves XML structure, including nested elements and attributes
- Handles XML namespaces
- Supports Unicode/UTF-8 encoding
- Provides command-line interface and programmatic usage
- Includes error handling for invalid XML
- Optional output file saving
- Pretty-printed JSON output with proper indentation

## Requirements

- Python 3.6+
- xmltodict library

Install the required package using:
```bash
pip install xmltodict
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Son0fSun/xmltojson.git
cd xmltojson
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command-line Usage

Convert an XML file:
```bash
python xml_to_json.py input.xml [output.json]
```

Convert an XML string:
```bash
python xml_to_json.py -s "<root><data>example</data></root>" [output.json]
```

### Programmatic Usage

```python
from xml_to_json import xml_to_json

# Using file
result = xml_to_json("input.xml", "output.json")

# Using string
xml_string = "<root><data>example</data></root>"
result = xml_to_json(xml_string, "output.json")
```

## Example

Input XML (example.xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <person id="1">
        <name>John Doe</name>
        <age>30</age>
        <address>
            <street>123 Main St</street>
            <city>New York</city>
        </address>
    </person>
</root>
```

Output JSON:
```json
{
  "root": {
    "person": {
      "@id": "1",
      "name": "John Doe",
      "age": "30",
      "address": {
        "street": "123 Main St",
        "city": "New York"
      }
    }
  }
}
```
