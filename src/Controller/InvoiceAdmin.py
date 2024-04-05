from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime
from PyQt6.QtCore import QDate

from View.InvoiceAdmin import Ui_InvoiceAdmin

from Model.Model_Invoice import Model_Invoice
from Model.Model_InvoiceDetail import Model_InvoiceDetail

class InvoiceAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_InvoiceAdmin()
        self.ui.setupUi(self)
        self.ui.date.setDisplayFormat("yyyy-MM-dd")
        self.ui.date.setDate(QDate.currentDate())

        self.iv = Model_Invoice()
        self.ivd = Model_InvoiceDetail()

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.account.clicked.connect(self.account)
        self.ui.employee.clicked.connect(self.employee)

        self.ui.select.clicked.connect(self.select)
        self.ui.detail.clicked.connect(self.detail)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)

    def setEnabled(self, bool):
        self.ui.invoiceID.setEnabled(bool)

    def statistic(self):
        pass

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

    def warranty(self):
        self.general.showWarrantyAdmin()
        self.general.page(3)

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

    def employee(self):
        self.general.showEmployeeAdmin()
        self.general.page(5)

    def select(self):
        self.setEnabled(False)
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow != -1:
            invoiceID = self.ui.table.item(self.selectRow, 0).text().strip()
            employeeID = self.ui.table.item(self.selectRow, 1).text().strip()
            customerID = self.ui.table.item(self.selectRow, 2).text().strip()
            date = self.ui.table.item(self.selectRow, 3).text().strip()
            totalCost = self.ui.table.item(self.selectRow, 4).text().strip()

            self.ui.invoiceID.setText(invoiceID)
            self.ui.employeeID.setText(employeeID)
            self.ui.customerID.setText(customerID)
            self.ui.date.setDate(QDate.fromString(date, "yyyy-MM-dd"))
            self.ui.totalCost.setText(totalCost)

    def detail(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Error", "Please select your import.")
            return
        
        self.general.invoiceDetail(self.getInvoice())
        self.general.page(22)

    def search(self):
        invoice = self.getInvoice()
        invoiceResult = self.iv.search(invoiceID=invoice["invoiceID"],
                                    employeeID=invoice["employeeID"],
                                    customerID=invoice["customerID"],
                                    date=invoice["date"],
                                    totalCost=invoice["totalCost"],
        )
        self.showData(invoiceResult)
    
    def showData(self, invoiceResult):
        self.ui.table.setRowCount(0)
        if invoiceResult:
            self.ui.table.setRowCount(len(invoiceResult))

            for row, info in enumerate(invoiceResult):
                infoList = [
                    info["invoiceID"],
                    info["employeeID"],
                    info["customerID"],
                    info["date"],
                    info["totalCost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getInvoice(self):
        invoiceID = self.ui.invoiceID.text().strip()
        employeeID = self.ui.employeeID.text().strip()
        customerID = self.ui.customerID.text().strip()
        date = self.ui.date.text().strip()
        totalCost = self.ui.totalCost.text().strip()

        invoice = {
            "invoiceID": invoiceID,
            "employeeID": employeeID,
            "customerID": customerID,
            "date": date,
            "totalCost": totalCost
        }

        return invoice

    def clear(self):
        self.selectRow = -1
        self.ui.invoiceID.clear()
        self.ui.employeeID.clear()
        self.ui.customerID.clear()
        self.ui.date.setDate(datetime.now().date())
        self.ui.totalCost.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select your invoice.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        invoice = self.getInvoice()
        invoiceID = invoice["invoiceID"]
        self.iv.delete(invoiceID)
        if self.ivd.checkExist(invoiceID):
            self.ivd.delete(invoiceID)
        QMessageBox.information(self, "Delete Confirmation", "Invoice has been deleted successfully.")
        self.clear()
