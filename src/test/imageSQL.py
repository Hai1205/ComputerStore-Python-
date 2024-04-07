from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QSizePolicy, QFrame, QMessageBox
from PyQt6.QtGui import QPixmap
import mysql.connector
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QByteArray
from PyQt6.QtGui import QImage, QPixmap
import base64


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 216, 721, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 721, 311))
        self.widget.setObjectName("widget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class ProductWidget(QWidget):
    def __init__(self, productID, image_data, quantity):
        super().__init__()
        self.productID = productID
        self.image_data = image_data
        self.quantity = quantity
        self.setupUi()

    def setupUi(self):
        # Create layout for the product widget
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to ensure no extra padding
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Set left alignment

        # Create frame for the product
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)  # Set frame shape
        frame.setLineWidth(2)  # Set border width

        frame_layout = QVBoxLayout(frame)
        frame_layout.setContentsMargins(10, 10, 10, 10)  # Add margins to frame layout
        frame_layout.setSpacing(10)  # Set spacing between widgets inside frame

        layout.addWidget(frame)  # Add product to the layout

        image_data = base64.b64decode(self.image_data)
        image = QImage.fromData(image_data)
        pixmap = QPixmap.fromImage(image)
        label_image = QLabel()
        label_image.setPixmap(pixmap.scaled(150, 150))
        frame_layout.addWidget(label_image, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Display product information
        label_info = QLabel(f"Product ID: {self.productID}\nQuantity: {self.quantity}")
        frame_layout.addWidget(label_info, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Connect mousePressEvent() to handle click event
        frame.mousePressEvent = self.on_clicked

    def on_clicked(self, event):
        QMessageBox.information(self, "Product Clicked", f"You clicked on {self.productID}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()

    def loadProducts(self):
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="computerstore"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT productID, image, quantity FROM product")  # Assuming 'image' is the column containing binary image data
        products = cursor.fetchall()
        cursor.close()
        conn.close()

        grid_layout = QGridLayout()  # Create a QGridLayout to hold the products
        grid_layout.setHorizontalSpacing(50)  # Set spacing between columns
        grid_layout.setVerticalSpacing(50)  # Set spacing between rows
        self.ui.scrollAreaWidgetContents.setLayout(grid_layout)

        row, column = 0, 0
        for product in products:
            productID = product[0].strip()
            image_data = product[1].strip()
            quantity = product[2]
            # Create a ProductWidget for each product
            product_widget = ProductWidget(productID, image_data, quantity)

            # Add the ProductWidget to the grid layout
            grid_layout.addWidget(product_widget, row, column)

            column += 1
            if column == 3:
                column = 0
                row += 1

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
