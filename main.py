import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

input_file, output_file = parse_arguments()
print(f"Plik wejściowy: {input_file}")
print(f"Plik wyjściowy: {output_file}")
