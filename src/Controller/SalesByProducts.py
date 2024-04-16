from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime

from View.SalesByProducts import Ui_SalesByProducts

from Model.Model_Product import Model_Product
from Model.Model_Invoice import Model_Invoice
from Model.Model_InvoiceDetail import Model_InvoiceDetail

class SalesByProducts(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SalesByProducts()
        self.ui.setupUi(self)

        self.pd = Model_Product()
        self.iv = Model_Invoice()
        self.ivd = Model_InvoiceDetail()

        self.totalCost = 0
        self.begin = datetime(datetime.now().year, 1, 1).date()

        self.button()

    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.salesByYears.clicked.connect(self.salesByYears)
        self.ui.salesByEmployees.clicked.connect(self.salesByEmployees)
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

    def salesByEmployees(self):
        self.general.showSalesByEmployees()
        self.general.page(25)
        
    def spendsByYears(self):
        self.general.showSpendsByYears()
        self.general.page(27)

    def spendsBySuppliers(self):
        self.general.showSpendsBySuppliers()
        self.general.page(28)

    def spendsByProducts(self):
        self.general.showSpendsByProducts()
        self.general.page(29)
    
    from datetime import datetime

    def cost(self, productID):
        cost = 0
        quantity = 0
        ivd = self.ivd.search(productID=productID, customerID="admin")
        for info in ivd:
            iv = self.iv.search(invoiceID=info["invoiceID"])
            date = iv[0]["date"]
            if self.begin <= date <= datetime.now().date():
                cost += info["cost"]
                quantity += info["quantity"]
        return cost, quantity

    def salesByProducts(self):
        staticResult = []
        ls = self.pd.search()
        for info in ls:
            productID = info["productID"]
            productName = info["productName"]
            cost, numberOfInvoice= self.cost(productID)
            self.totalCost += cost
            info = (productID, productName, cost, numberOfInvoice)
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