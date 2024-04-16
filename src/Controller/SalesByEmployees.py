from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime

from View.SalesByEmployees import Ui_SalesByEmployees

from Model.Model_Employee import Model_Employee
from Model.Model_Invoice import Model_Invoice

class SalesByEmployees(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SalesByEmployees()
        self.ui.setupUi(self)

        self.ep = Model_Employee()
        self.iv = Model_Invoice()

        self.totalCost = 0
        self.begin = datetime(datetime.now().year, 1, 1).date()

        self.button()

    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.salesByYears.clicked.connect(self.salesByYears)
        self.ui.salesByProducts.clicked.connect(self.salesByProducts)
        self.ui.spendsByYears.clicked.connect(self.spendsByYears)
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

    def salesByProducts(self):
        self.general.showCustomerAdmin()
        self.general.page(26)

    def spendsByYears(self):
        self.general.showsalesByProducts()
        self.general.page(27)

    def spendsBySuppliers(self):
        self.general.showSpendsBySuppliers()
        self.general.page(28)

    def spendsByProducts(self):
        self.general.showSpendsByProducts()
        self.general.page(29)

    def cost(self, employeeID):
        ls = self.iv.search(employeeID=employeeID)
        cost = 0
        count = 0
        for info in ls:
            date = info["date"]
            if self.begin <= date <= datetime.now().date():
                cost += info["totalCost"]
                count += 1
        return cost, count

    def salesByEmployees(self):
        staticResult = []
        ls = self.ep.search(position="Sale")
        for info in ls:
            employeeID = info["employeeID"]
            name = info["firstname"] + " " + info["lastname"]
            cost, numberOfInvoice= self.cost(employeeID)
            self.totalCost += cost
            info = (employeeID, name, cost, numberOfInvoice)
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