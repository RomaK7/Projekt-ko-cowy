import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

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
        
        # Wywołaj odpowiednie funkcje do wczytania i zapisu danych
        # np. read_json_file(input_file), write_json_file(data, output_file)
        
        print("Konwersja zakończona.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())
