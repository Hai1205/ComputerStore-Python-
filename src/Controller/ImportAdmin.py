from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime
from PyQt6.QtCore import QDate

from View.ImportAdmin import Ui_ImportAdmin

from Model.Model_Import import Model_Import
from Model.Model_ImportDetail import Model_ImportDetail

from Controller.Controller import Controller

class ImportAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_ImportAdmin()
        self.ui.setupUi(self)
        self.ui.date.setDisplayFormat("yyyy-MM-dd")
        self.ui.date.setDate(QDate.currentDate())

        self.ip = Model_Import()
        self.ipd = Model_ImportDetail()

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.account.clicked.connect(self.account)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.employee.clicked.connect(self.employee)

        self.ui.select.clicked.connect(self.select)
        self.ui.detail.clicked.connect(self.detail)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)
    
    def setEnabled(self, bool):
        self.ui.importID.setEnabled(bool)

    def statistic(self):
        self.general.showSalesByYears()
        self.general.page(24)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def product(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

    def customer(self):
        self.general.showCustomerAdmin()
        self.general.page(4)

    def supplier(self):
        self.general.showSupplierAdmin()
        self.general.page(8)

    def warranty(self):
        self.general.showWarrantyAdmin()
        self.general.page(3)

    def invoice(self):
        self.general.showInvoiceAdmin()
        self.general.page(9)

    def employee(self):
        self.general.showEmployeeAdmin()
        self.general.page(5)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a import.")
            return
        
        self.setEnabled(False)
        importID = self.ui.table.item(self.selectRow, 0).text().strip()
        employeeID = self.ui.table.item(self.selectRow, 1).text().strip()
        supplierID = self.ui.table.item(self.selectRow, 2).text().strip()
        date = self.ui.table.item(self.selectRow, 3).text().strip()
        totalCost = self.ui.table.item(self.selectRow, 4).text().strip()

        self.ui.importID.setText(importID)
        self.ui.employeeID.setText(employeeID)
        self.ui.supplierID.setText(supplierID)
        self.ui.date.setDate(QDate.fromString(date, "yyyy-MM-dd"))
        self.ui.totalCost.setText(totalCost)

    def detail(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Error", "Please select a import.")
            return
        
        self.general.importDetail(self.getImport())
        self.general.page(23)

    def search(self):
        import_2 = self.getImport()
        importResult = self.ip.search(importID=import_2["importID"],
                                    employeeID=import_2["employeeID"],
                                    supplierID=import_2["supplierID"],
                                    date=import_2["date"],
                                    totalCost=import_2["totalCost"],
        )
        self.showData(importResult)
    
    def showData(self, importResult):
        self.ui.table.setRowCount(0)
        if importResult:
            self.ui.table.setRowCount(len(importResult))

            for row, info in enumerate(importResult):
                infoList = [
                    info["importID"],
                    info["employeeID"],
                    info["supplierID"],
                    info["date"],
                    info["totalCost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getImport(self):
        importID = self.ui.importID.text().strip()
        employeeID = self.ui.employeeID.text().strip()
        supplierID = self.ui.supplierID.text().strip()
        date = self.ui.date.text().strip()
        totalCost = self.ui.totalCost.text().strip()

        import_2 = {
            "importID": importID,
            "employeeID": employeeID,
            "supplierID": supplierID,
            "date": date,
            "totalCost": totalCost
        }

        return import_2

    def clear(self):
        self.selectRow = -1
        self.ui.importID.clear()
        self.ui.employeeID.clear()
        self.ui.supplierID.clear()
        self.ui.date.setDate(datetime.now().date())
        self.ui.totalCost.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select a import.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        import_2 = self.getImport()
        importID = import_2["importID"]
        self.ip.delete(importID)
        if self.ipd.checkExist(importID):
            self.ipd.delete(importID)
        QMessageBox.information(self, "Delete Confirmation", "Import has been deleted successfully.")
        self.clear()
