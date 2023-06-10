import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Błąd parsowania pliku YAML: {e}")
            return None

yaml_data = read_yaml_file(input_file)
if yaml_data:
    print("Dane z pliku YAML:")
    print(yaml_data)
