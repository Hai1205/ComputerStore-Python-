import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ứng dụng ở chính giữa màn hình")

        # Lấy kích thước của màn hình
        screen = QDesktopWidget().screenGeometry()

        # Lấy kích thước của cửa sổ ứng dụng
        window_size = self.geometry()

        # Tính toán vị trí để đặt cửa sổ ở giữa màn hình
        x = (screen.width() - window_size.width()) / 2
        y = (screen.height() - window_size.height()) / 2

        # Đặt vị trí của cửa sổ
        self.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
