import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import concurrent.futures

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

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

def write_xml_file(data, file_path):
    root = ET.Element("root")
    root.append(data)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Dane zapisane do pliku XML.")

class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter danych")
        self.setGeometry(100, 100, 300, 150)
        
        self.input_label = QLabel("Plik wejściowy:", self)
        self.input_field = QLineEdit(self)
        
        self.output_label = QLabel("Plik wyjściowy:", self)
        self.output_field = QLineEdit(self)
        
        self.convert_button = QPushButton("Konwertuj", self)
        self.convert_button.clicked.connect(self.convert_data)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(self.convert_button)
        
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def convert_data(self):
        input_file = self.input_field.text()
        output_file = self.output_field.text()
        
        if input_file.endswith('.json'):
            json_data = read_json_file(input_file)
            if json_data:
                write_json_file(json_data, output_file)
        
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            yaml_data = read_yaml_file(input_file)
            if yaml_data:
                write_yaml_file(yaml_data, output_file)
        
        elif input_file.endswith('.xml'):
            xml_data = read_xml_file(input_file)
            if xml_data:
                write_xml_file(xml_data, output_file)
        
        else:
            print("Nieobsługiwany format pliku.")
        
        print("Konwersja zakończona.")

def convert_data_async(input_file, output_file):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if input_file.endswith('.json'):
            read_future = executor.submit(read_json_file, input_file)
            json_data = read_future.result()
            write_future = executor.submit(write_json_file, json_data, output_file)
            write_future.result()
        
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            read_future = executor.submit(read_yaml_file, input_file)
            yaml_data = read_future.result()
            write_future = executor.submit(write_yaml_file, yaml_data, output_file)
            write_future.result()
        
        elif input_file.endswith('.xml'):
            read_future = executor.submit(read_xml_file, input_file)
            xml_data = read_future.result()
            write_future = executor.submit(write_xml_file, xml_data, output_file)
            write_future.result()
        
        else:
            print("Nieobsługiwany format pliku.")
        
        print("Konwersja zakończona.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.convert_button.clicked.connect(lambda: convert_data_async(window.input_field.text(), window.output_field.text()))
    window.show()
    sys.exit(app.exec())
