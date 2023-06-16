import argparse
import json
import yaml
import xml.etree.ElementTree as ET
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

input_file, output_file = parse_arguments()

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd dekodowania pliku JSON: {e}")
            return None

def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Dane zapisane do pliku JSON.")

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Błąd parsowania pliku YAML: {e}")
            return None

def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
    print("Dane zapisane do pliku YAML.")

def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd parsowania pliku XML: {e}")
        return None
