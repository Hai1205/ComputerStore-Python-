from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate
from datetime import datetime, timedelta

from View.WarrantyAdmin import Ui_WarrantyAdmin

from Model.Model_Warranty import Model_Warranty

from Controller.Controller import Controller

class WarrantyAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_WarrantyAdmin()
        self.ui.setupUi(self)

        self.wrt = Model_Warranty()

        self.customerID = None
        self.purchaseDate = datetime.now()
        self.ui.purchaseDate.setDisplayFormat("yyyy-MM-dd")
        self.ui.purchaseDate.setDate(QDate.currentDate())
        self.ui.EXP.setDisplayFormat("yyyy-MM-dd")
        EXP = datetime.now() + timedelta(days=24*30+10)
        self.ui.EXP.setDate(EXP.date())

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.account.clicked.connect(self.account)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.employee.clicked.connect(self.employee)

        self.ui.select.clicked.connect(self.select)
        self.ui.add.clicked.connect(self.add)
        self.ui.expiryList.clicked.connect(self.expiryList)
        self.ui.update.clicked.connect(self.update)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)
    
    def setCustomerID(self, customerID):
        self.customerID = customerID

    def statistic(self):
        self.general.page(24)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def product(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def import_2(self):
        self.general.showImportAdmin()
        self.general.page(6)

    def customer(self):
        self.general.showCustomerAdmin()
        self.general.page(4)

    def supplier(self):
        self.general.showSupplierAdmin()
        self.general.page(8)

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

    def invoice(self):
        self.general.showInvoiceAdmin()
        self.general.page(9)

    def employee(self):
        self.general.showEmployeeAdmin()
        self.general.page(5)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a warranty.")
            return
        
        self.setEnabled(False)
        warrantyID = self.ui.table.item(self.selectRow, 0).text().strip()
        productID = self.ui.table.item(self.selectRow, 1).text().strip()
        invoiceID = self.ui.table.item(self.selectRow, 2).text().strip()
        customerID = self.ui.table.item(self.selectRow, 3).text().strip()
        purchaseDate = self.ui.table.item(self.selectRow, 4).text().strip()
        warrantyTime = self.ui.table.item(self.selectRow, 5).text().strip()
        EXP = self.ui.table.item(self.selectRow, 6).text().strip()

        self.ui.warrantyID.setText(warrantyID)
        self.ui.productID.setText(productID)
        self.ui.invoiceID.setText(invoiceID)
        self.ui.customerID.setText(customerID)
        self.ui.purchaseDate.setDate(QDate.fromString(purchaseDate, "yyyy-MM-dd"))
        self.ui.warrantyTime.setText(warrantyTime)
        self.ui.EXP.setDate(QDate.fromString(EXP, "yyyy-MM-dd"))
    
    def add(self):
        warranty = self.getWarranty()
        warrantyID = warranty["warrantyID"]
        productID = warranty["productID"]
        invoiceID = warranty["invoiceID"]
        customerID = warranty["customerID"]
        warrantyTime = warranty["warrantyTime"]

        if warrantyID:
            QMessageBox.information(self, "Add Error", "Infornation cannot be entered WarrantyID.")
            return
        elif not productID:
            QMessageBox.information(self, "Add Error", "ProductID can not be blank.")
            return
        elif not invoiceID:
            QMessageBox.information(self, "Add Error", "InvoiceID can not be blank.")
            return
        elif not customerID:
            QMessageBox.information(self, "Add Error", "CustomerID can not be blank.")
            return
        elif not warrantyTime:
            QMessageBox.information(self, "Add Error", "Warranty time can not be blank.")
            return
        elif not warrantyTime.isdigit():
            QMessageBox.warning(self, "Add Error", "Please enter an integer value into a warranty time.")
            return

        while True:
            warrantyID = Controller.createWarrantyID()
            if not self.wrt.checkExist(warrantyID):
                break
        exp = self.purchaseDate + timedelta(days=int(warrantyTime)*30+10)
        EXP = exp.date()
        
        self.wrt.add(warrantyID, productID, invoiceID, customerID, self.purchaseDate.date(), int(warrantyTime), EXP)

        QMessageBox.information(self, "Add Confirmation", "Warranty has been added successfully.")
        self.clear()

    def expiryList(self):
        warranty = self.getWarranty()

        purchaseDate = warranty["purchaseDate"]
        if Controller.compare_dates(datetime.strptime(purchaseDate, "%Y-%m-%d").date(), datetime(2000, 1, 1).date()):
            purchaseDate = None
        EXP = warranty["EXP"]
        if Controller.compare_dates(datetime.strptime(EXP, "%Y-%m-%d").date(), datetime(2000, 1, 1).date()):
            EXP = None

        warrrantyResult = self.wrt.expiryList(warrantyID=warranty["warrantyID"],
                                        productID=warranty["productID"],
                                        invoiceID=warranty["invoiceID"],
                                        customerID=self.customerID,
                                        purchaseDate=purchaseDate,
                                        warrantyTime=warranty["warrantyTime"],
                                        EXP=EXP
        )
        self.showData(warrrantyResult)

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select a waranty.")
            return
        
        warranty = self.getWarranty()
        warrantyID = warranty["warrantyID"]
        purchaseDate = warranty["purchaseDate"]
        warrantyTime = warranty["warrantyTime"]

        if not warrantyTime.isdigit():
            QMessageBox.warning(self, "Warning", "Please enter an integer value into a warranty time.")
            return

        self.wrt.update(warrantyID, purchaseDate, int(warrantyTime))
        self.search()
    
    def setEnabled(self, bool):
        self.ui.warrantyID.setEnabled(bool)
        self.ui.productID.setEnabled(bool)
        self.ui.invoice.setEnabled(bool)
        self.ui.customerID.setEnabled(bool)
        self.ui.EXP.setEnabled(bool)
        self.ui.add.setEnabled(bool)

    def search(self):
        warranty = self.getWarranty()
        customerID = warranty["customerID"]
        if customerID == "":
            customerID = self.customerID

        warrrantyResult = self.wrt.search(warrantyID=warranty["warrantyID"],
                                        productID=warranty["productID"],
                                        invoiceID=warranty["invoiceID"],
                                        customerID=customerID,
                                        purchaseDate=warranty["purchaseDate"],
                                        warrantyTime=warranty["warrantyTime"],
                                        EXP=warranty["EXP"]
        )
        self.showData(warrrantyResult)
    
    def showData(self, warrrantyResult):
        self.ui.table.setRowCount(0)
        if warrrantyResult:
            self.ui.table.setRowCount(len(warrrantyResult))

            for row, info in enumerate(warrrantyResult):
                infoList = [
                    info["warrantyID"],
                    info["productID"],
                    info["invoiceID"],
                    info["customerID"],
                    info["purchaseDate"],
                    info["warrantyTime"],
                    info["EXP"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getWarranty(self):
        warrantyID = self.ui.warrantyID.text().strip()
        productID = self.ui.productID.text().strip()
        invoiceID = self.ui.invoiceID.text().strip()
        customerID = self.ui.customerID.text().strip()
        purchaseDate = self.ui.purchaseDate.text().strip()
        warrantyTime = self.ui.warrantyTime.text().strip()
        EXP = self.ui.EXP.text().strip()

        warranty = {
            "warrantyID": warrantyID,
            "productID": productID,
            "invoiceID": invoiceID,
            "customerID": customerID,
            "purchaseDate": purchaseDate,
            "warrantyTime": warrantyTime,
            "EXP": EXP
        }

        return warranty

    def clear(self):
        self.selectRow = -1
        self.ui.warrantyID.clear()
        self.ui.productID.clear()
        self.ui.invoiceID.clear()
        self.ui.customerID.clear()
        self.ui.warrantyTime.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select a warranty.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        warranty = self.getWarranty()
        warrantyID = warranty["warrantyID"]
        self.wrt.delete(warrantyID)
        QMessageBox.information(self, "Delete Confirmation", "Warranty has been deleted successfully.")
        self.clear()
