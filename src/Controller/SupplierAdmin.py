from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from View.SupplierAdmin import Ui_SupplierAdmin

from Model.Model_Supplier import Model_Supplier

from Controller.Controller import Controller

class SupplierAdmin(QMainWindow):
    def __init__(self, general=None):
        super().__init__()
        self.general = general
        self.ui = Ui_SupplierAdmin()
        self.ui.setupUi(self)

        self.sp = Model_Supplier()

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.account.clicked.connect(self.account)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.employee.clicked.connect(self.employee)

        self.ui.select.clicked.connect(self.select)
        self.ui.add.clicked.connect(self.add)
        self.ui.update.clicked.connect(self.update)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)


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

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

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
        self.setEnabled(False)
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow != -1:
            supplierID = self.ui.table.item(self.selectRow, 0).text().strip()
            supplierName = self.ui.table.item(self.selectRow, 1).text().strip()

            self.ui.supplierID.setText(supplierID)
            self.ui.supplierName.setText(supplierName)

    def add(self):
        supplier = self.getSupplier()
        supplierID = ""
        if supplierID == "":
            while True:
                supplierID = Controller.createSupplierID()
                if not self.sp.checkExist(supplierID):
                    break
        supplierName = supplier["supplierName"]

        self.sp.add(supplierID, supplierName)

        QMessageBox.information(self, "Add Confirmation", "Customer has been added successfully.")
        self.clear()

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select your import.")
            return
        
        supplier = self.getSupplier()
        supplierID = supplier["supplierID"]
        supplierName = supplier["supplierName"]

        self.sp.update(supplierID, supplierName)
        self.search()

    def search(self):
        supplier = self.getSupplier()
        supplierResult = self.sp.search(supplierID=supplier["supplierID"],
                                    supplierName=supplier["supplierName"],
        )
        self.showData(supplierResult)

    def showData(self, supplierResult):
        self.ui.table.setRowCount(0)
        if supplierResult:
            self.ui.table.setRowCount(len(supplierResult))

            for row, info in enumerate(supplierResult):
                infoList = [
                    info["supplierID"],
                    info["supplierName"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getSupplier(self):
        supplierID = self.ui.supplierID.text().strip()
        supplierName = self.ui.supplierName.text().strip()

        supplier = {
            "supplierID": supplierID,
            "supplierName": supplierName
        }

        return supplier

    def setEnabled(self, bool):
        self.ui.supplierID.setEnabled(bool)

    def clear(self):
        self.selectRow = -1
        self.ui.supplierID.clear()
        self.ui.supplierName.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select the supplier.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        supplier = self.getSupplier()
        supplierID = supplier["supplierID"]
        self.sp.delete(supplierID)
        QMessageBox.information(self, "Delete Confirmation", "Supplier has been deleted successfully.")
        self.clear()

    def updateCombobox(self):
        result = self.sp.search()
        list = ["All"]
        for i in result:
            list.append(i["supplierName"])
        return list
