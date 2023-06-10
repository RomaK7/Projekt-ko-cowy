import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd dekodowania pliku JSON: {e}")
            return None

json_data = read_json_file(input_file)
if json_data:
    print("Dane z pliku JSON:")
    print(json_data)
