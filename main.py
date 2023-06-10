import xml.etree.ElementTree as ET

def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd parsowania pliku XML: {e}")
        return None

xml_data = read_xml_file(input_file)
if xml_data:
    print("Dane z pliku XML:")
    print(ET.tostring(xml_data, encoding='unicode'))
