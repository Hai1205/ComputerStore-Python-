from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QByteArray, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to Binary")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_button)

        self.convert_button = QPushButton("Convert to Binary")
        self.convert_button.clicked.connect(self.convert_to_binary)
        layout.addWidget(self.convert_button)

        self.binary_label = QLabel()
        layout.addWidget(self.binary_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def upload_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Image files (*.jpg *.jpeg *.png *.bmp *.gif)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

            # Convert image to binary
            with open(file_path, 'rb') as f:
                byte_array = QByteArray(f.read())
                self.image_binary = byte_array.toBase64().data().decode()

    def convert_to_binary(self):
        if hasattr(self, 'image_binary'):
            print(self.image_binary)
        else:
            self.binary_label.setText("Please upload an image first.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
