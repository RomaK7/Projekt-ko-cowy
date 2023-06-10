import concurrent.futures

def convert_data_async(input_file, output_file):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Wywołaj funkcje wczytujące dane w oddzielnym wątku
        read_future = executor.submit(read_json_file, input_file)
        json_data = read_future.result()  # Poczekaj na zakończenie wczytywania
        
        # Wywołaj funkcje zapisujące dane w oddzielnym wątku
        write_future = executor.submit(write_json_file, json_data, output_file)
        write_future.result()  # Poczekaj na zakończenie zapisu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.convert_button.clicked.connect(lambda: convert_data_async(window.input_field.text(), window.output_field.text()))
    window.show()
    sys.exit(app.exec())
