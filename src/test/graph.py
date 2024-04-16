import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt


class Graph4:
    def __init__(self, parent=None):
        self.parent = parent
        
    def show(self):
        # Data for the bar chart
        years = ['2019', '2020', '2021', '2022', '2023']
        values = [100, 150, 200, 180, 220]

        # Create a bar chart
        plt.bar(years, values, color='b')
        plt.xlabel('Years')
        plt.ylabel('Total cost')
        plt.title('Sales by Years')

        # Save the chart to a temporary file
        temp_file = 'temp_chart.png'
        plt.savefig(temp_file)

        # Load the chart image into QPixmap
        chart_pixmap = QPixmap(temp_file)

        # Set the chart image to the label
        self.parent.graph_label.setPixmap(chart_pixmap)

        # Clean up: close the plot and remove the temporary file
        plt.close()
        import os
        os.remove(temp_file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Sales by Years")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a label for the graph
        self.graph_label = QLabel()
        layout.addWidget(self.graph_label)

        # Create the graph and display it
        graph = Graph4(parent=self)
        graph.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
