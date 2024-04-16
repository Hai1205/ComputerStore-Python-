from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QPushButton, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


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
        self.select = QtWidgets.QPushButton(parent=self.centralwidget)
        self.select.setGeometry(QtCore.QRect(70, 160, 93, 28))
        self.select.setObjectName("select")
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
        self.select.setText(_translate("MainWindow", "select"))


class ProductWidget(QWidget):
    def __init__(self, index, name, image_path, information):
        super().__init__()
        self.index = index
        self.name = name
        self.image_path = image_path
        self.information = information
        self.setupUi()

    def setupUi(self):
        # Tạo layout cho widget sản phẩm
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  

        # Tạo frame cho sản phẩm
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box) 
        frame.setLineWidth(2)  

        frame_layout = QVBoxLayout(frame)
        frame_layout.setContentsMargins(10, 10, 10, 10)  
        frame_layout.setSpacing(10)  

        layout.addWidget(frame)  

        # Hiển thị hình ảnh
        label_image = QLabel()
        pixmap = QPixmap(self.image_path)
        label_image.setPixmap(pixmap.scaled(150, 150))  
        frame_layout.addWidget(label_image, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Hiển thị thông tin
        label_info = QLabel(self.information)
        frame_layout.addWidget(label_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Kết nối sự kiện nhấp chuột để xử lý
        frame.mousePressEvent = self.on_clicked

    def on_clicked(self, event):
        parent_widget = self.parentWidget().parentWidget()  # Lấy đối tượng MainWindow từ ProductWidget
        parent_widget.on_select_clicked(self.index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.select.clicked.connect(self.on_select_clicked)
    
    def on_select_clicked(self, index):
        print(f"Selected product index: {index}")

    def loadProducts(self):
        name = "LO"
        info = f"""
Supplier name: Asus
Product name: {name}
Type: Laptop
Quantity: 10
Warranty time: 24
Price: 500"""
        products = [
            {"name": "111111111112", "image_path": "../ComputerStore/src/test/R.jpg", "information": f"{info}"},
            {"name": "111111111113", "image_path": "../ComputerStore/src/test/R.jpg", "information": """
Supplier name: Asus
Product name: LOL
Type: Laptop
Quantity: 10
Warranty time: 24
Price: 500"""}
            # Add more products as needed...
        ]

        grid_layout = QGridLayout()  
        grid_layout.setHorizontalSpacing(50) 
        grid_layout.setVerticalSpacing(50) 
        self.ui.scrollAreaWidgetContents.setLayout(grid_layout)

        for index, product in enumerate(products):
            name = product["name"]
            image_path = product["image_path"]
            information = product["information"]

            product_widget = ProductWidget(index, name, image_path, information)
            row = index // 3
            column = index % 3
            grid_layout.addWidget(product_widget, row, column)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
