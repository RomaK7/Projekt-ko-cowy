def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
    print("Dane zapisane do pliku YAML.")

write_yaml_file(yaml_data, output_file)
