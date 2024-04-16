from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime

from View.SpendsByProducts import Ui_SpendsByProducts

from Model.Model_Product import Model_Product
from Model.Model_Import import Model_Import
from Model.Model_ImportDetail import Model_ImportDetail

class SpendsByProducts(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SpendsByProducts()
        self.ui.setupUi(self)

        self.pd = Model_Product()
        self.ip = Model_Import()
        self.ipd = Model_ImportDetail()

        self.totalCost = 0
        self.begin = datetime(datetime.now().year, 1, 1).date()

        self.button()

    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.salesByYears.clicked.connect(self.salesByYears)
        self.ui.salesByEmployees.clicked.connect(self.salesByEmployees)
        self.ui.salesByProducts.clicked.connect(self.salesByProducts)
        self.ui.spendsByYears.clicked.connect(self.spendsByYears)
        self.ui.spendsBySuppliers.clicked.connect(self.spendsBySuppliers)

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

    def spendsByYears(self):
        self.general.showSpendsByYears()
        self.general.page(27)

    def spendsBySuppliers(self):
        self.general.showSpendsBySuppliers()
        self.general.page(28)
    
    def cost(self, productID):
        cost = 0
        quantity = 0
        ipd = self.ipd.search(productID=productID)
        for info in ipd:
            ip = self.ip.search(importID=info["importID"])
            date = ip[0]["date"]
            if self.begin <= date <= datetime.now().date():
                cost += info["cost"]
                quantity += info["quantity"]
        return cost, quantity

    def spendsByProducts(self):
        staticResult = []
        ls = self.pd.search()
        for info in ls:
            productID = info["productID"]
            productName = info["productName"]
            cost, numberOfImport= self.cost(productID)
            self.totalCost += cost
            info = (productID, productName, cost, numberOfImport)
            staticResult.append(info)
        self.showData(staticResult)
    
    def showData(self, staticResult):
        self.ui.table.setRowCount(0)
        self.ui.totalCost.setText(str(self.totalCost))

        if staticResult:
            self.ui.table.setRowCount(len(staticResult))

            for row, info in enumerate(staticResult):
                infoList = [
                    info[0],
                    info[1],
                    info[2],
                    info[3],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return