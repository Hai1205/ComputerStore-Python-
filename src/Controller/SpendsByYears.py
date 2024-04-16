from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt

from View.SpendsByYears import Ui_SpendsByYears

from Model.Model_Import import Model_Import

class SpendsByYears(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SpendsByYears()
        self.ui.setupUi(self)
        self.ip = Model_Import()

        self.button()

    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.salesByYears.clicked.connect(self.salesByYears)
        self.ui.salesByEmployees.clicked.connect(self.salesByEmployees)
        self.ui.salesByProducts.clicked.connect(self.salesByProducts)
        self.ui.spendsBySuppliers.clicked.connect(self.spendsBySuppliers)
        self.ui.spendsByProducts.clicked.connect(self.spendsByProducts)

    def management(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)
    
    def salesByYears(self):
        self.general.showSalesByYears()
        self.general.page(24)

    def salesByEmployees(self):
        self.general.showSalesByEmployees()
        self.general.page(25)

    def salesByProducts(self):
        self.general.showsalesByProducts()
        self.general.page(26)

    def spendsBySuppliers(self):
        self.general.showSpendsBySuppliers()
        self.general.page(28)

    def spendsByProducts(self):
        self.general.showSpendsByProducts()
        self.general.page(29)
    
    def spendsByYears(self):
        total, listTotal = self.getTotal()
        listYears = self.getYears()
        # listTotal = [100, 150, 200, 180, 220]
        # listYears = ['2019', '2020', '2021', '2022', '2023']
        self.ui.totalCost.setText(str(total) + " USD")

        plt.figure(figsize=(7, 4.2))

        width = 0.5

        plt.bar(listYears, listTotal, color='skyblue', width=width)
        plt.xlabel('Years', fontsize=14)
        plt.ylabel('Total cost', fontsize=14)
        plt.title('Sales by Years', fontsize=16)
        plt.grid(True, linestyle='--', alpha=0.7)

        for i in range(len(listYears)):
            total_float = float(listTotal[i])
            plt.text(listYears[i], total_float + 0.5, str(total_float), ha='center', va='bottom')

        tempFile = 'tempChart.png'
        plt.savefig(tempFile, bbox_inches='tight')

        chartPixmap = QPixmap(tempFile)
        self.ui.graph.setPixmap(chartPixmap)

        plt.close()
        import os
        os.remove(tempFile)

    def getTotal(self):
        result = self.ip.getYearsAndTotal()
        listTotal = []
        total = 0
        for i in result:
            listTotal.append(i["total"])
            total += i["total"]
        return total, listTotal
    
    def getYears(self):
        result = self.ip.getYearsAndTotal()
        listYears = []
        for i in result:
            listYears.append(i["year"])
        return listYears