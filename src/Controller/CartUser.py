from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime

from View.CartUser import Ui_CartUser

from Model.Model_InvoiceDetail import Model_InvoiceDetail
from Model.Model_Invoice import Model_Invoice
from Model.Model_Product import Model_Product
from Model.Model_Warranty import Model_Warranty

class CartUser(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_CartUser()
        self.ui.setupUi(self)
        
        self.ivd = Model_InvoiceDetail()
        self.iv = Model_Invoice()
        self.pd = Model_Product()
        self.wrt = Model_Warranty()

        self.selectRow = -1
        self.customerID = None
        
        self.button()
    
    def setCustomerID(self, customerID):
        self.customerID = customerID
    
    def setEnabled(self, bool):
        self.ui.invoiceID.setEnabled(bool)
        self.ui.productID.setEnabled(bool)
        self.ui.warrantyID.setEnabled(bool)
        self.ui.quantity.setEnabled(bool)
        self.ui.price.setEnabled(bool)
        self.ui.cost.setEnabled(bool)

    def button(self):
        self.ui.product.clicked.connect(self.product)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.setting.clicked.connect(self.setting)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.select.clicked.connect(self.select)
        self.ui.refund.clicked.connect(self.refund)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)

    def product(self):
        self.general.showProductUser()
        self.general.page(11)
    
    def warranty(self):
        self.general.showWarrantyUser()
        self.general.page(13)

    def setting(self):
        self.general.showSettingUser()
        self.general.page(12)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a invoice detail.")
            return
        
        self.setEnabled(False)
        invoiceID = self.ui.table.item(self.selectRow, 0).text().strip()
        productID = self.ui.table.item(self.selectRow, 1).text().strip()
        warrantyID = self.ui.table.item(self.selectRow, 2).text().strip()
        quantity = self.ui.table.item(self.selectRow, 3).text().strip()
        price = self.ui.table.item(self.selectRow, 4).text().strip()
        cost = self.ui.table.item(self.selectRow, 5).text().strip()

        self.ui.invoiceID.setText(invoiceID)
        self.ui.productID.setText(productID)
        self.ui.warrantyID.setText(warrantyID)
        self.ui.price.setText(price)
        self.ui.quantity.setText(quantity)
        self.ui.cost.setText(cost)

    def refund(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Refund Error", "Please select your invoice detail.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to refund?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        invoiceDetail = self.getInvoiceDetail()
        invoiceID = invoiceDetail["invoiceID"]
        productID = invoiceDetail["productID"]
        warrantyID = invoiceDetail["warrantyID"]
        quantity = invoiceDetail["quantity"]
        cost = invoiceDetail["cost"]

        result = self.iv.getDate(invoiceID)
        date = result["date"]
        now = datetime.now().date()
        delta = now - date
        
        days = abs(delta.days)
        if days > 7:
            QMessageBox.information(self, "Refund Error", "Refund can only be made within 7 days.")
            return

        self.pd.increaseQuantity(productID, quantity)
        self.iv.decreaseTotalCost(invoiceID, cost)
        self.wrt.delete(warrantyID)
        self.ivd.delete(warrantyID)
        QMessageBox.information(self, "Refund Confirmation", "Refund has been placed successfully.")
        self.clear()

    def search(self):
        invoiceDetail = self.getInvoiceDetail()
        invoiceDetailResult = self.ivd.search(invoiceID=invoiceDetail["invoiceID"],
                                              productID=invoiceDetail["productID"],
                                              warrantyID=invoiceDetail["warrantyID"],
                                              customerID=self.customerID,
                                              quantity=invoiceDetail["quantity"],
                                              price=invoiceDetail["price"],
                                              cost=invoiceDetail["cost"]
        )
        self.showData(invoiceDetailResult)

    def showData(self, invoiceDetailResult):
        self.ui.table.setRowCount(0)
        if invoiceDetailResult:
            self.ui.table.setRowCount(len(invoiceDetailResult))

            for row, info in enumerate(invoiceDetailResult):
                infoList = [
                    info["invoiceID"],
                    info["productID"],
                    info["warrantyID"],
                    info["quantity"],
                    info["price"],
                    info["cost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
    
    def getInvoiceDetail(self):
        invoiceID = self.ui.invoiceID.text().strip()
        productID = self.ui.productID.text().strip()
        warrantyID = self.ui.warrantyID.text().strip()
        quantity = self.ui.quantity.text().strip()
        price = self.ui.price.text().strip()
        cost = self.ui.cost.text().strip()

        invoiceDetail = {
            "invoiceID": invoiceID,
            "productID": productID,
            "warrantyID": warrantyID,
            "quantity": quantity,
            "price": price,
            "cost": cost,
        }  

        return invoiceDetail

    def showData(self, invoiceDetailResult):
        self.ui.table.setRowCount(0)
        if invoiceDetailResult:
            self.ui.table.setRowCount(len(invoiceDetailResult))

            for row, info in enumerate(invoiceDetailResult):
                infoList = [
                    info["invoiceID"],
                    info["productID"],
                    info["warrantyID"],
                    info["quantity"],
                    info["price"],
                    info["cost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return

    def clear(self):
        self.ui.invoiceID.clear()
        self.ui.productID.clear()
        self.ui.warrantyID.clear()
        self.ui.quantity.clear()
        self.ui.price.clear()
        self.ui.cost.clear()
        self.selectRow = -1
        self.search()
        self.setEnabled(True)