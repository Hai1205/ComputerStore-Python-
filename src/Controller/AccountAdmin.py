from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from View.AccountAdmin import Ui_AccountAdmin

from Model.Model_Account import Model_Account
from Model.Model_Customer import Model_Customer

from Controller.Controller import Controller

class AccountAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_AccountAdmin()
        self.ui.setupUi(self)

        self.acc = Model_Account()
        self.ctm = Model_Customer()

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
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

    def invoice(self):
        self.general.showInvoiceAdmin()
        self.general.page(9)

    def employee(self):
        self.general.showEmployeeAdmin()
        self.general.page(5)
    
    def setEnabled(self, bool):
        self.ui.username.setEnabled(bool)
        self.ui.customerID.setEnabled(bool)
        self.ui.add.setEnabled(bool)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a account.")
            return

        self.setEnabled(False)
        username = self.ui.table.item(self.selectRow, 0).text().strip()
        password = self.ui.table.item(self.selectRow, 1).text().strip()
        customerID = self.ui.table.item(self.selectRow, 2).text().strip()

        self.ui.username.setText(username)
        self.ui.password.setText(password)
        self.ui.customerID.setText(customerID)

    def add(self):
        account = self.getAccount()
        username = account["username"]
        password = account["password"]
        customerID  = account["customerID"]

        if not username:
            QMessageBox.information(self, "Add Error", "Username can not be blank.")
            return
        elif not Controller.checkUsername(username):
            QMessageBox.information(self, "Sign up fail", """Please enter the username does not contain: 
Space
Special characters.""")
            return
        elif self.acc.checkExist(username):
            QMessageBox.information(self, "Sign up fail", "Username already exists")
            return
        elif not password:
            QMessageBox.information(self, "Add Error", "Password can not be blank.")
            return
        elif not Controller.checkPassword(password):
            QMessageBox.information(self, "Sign up fail", """Please enter the password with: 
At least 6 characters
At least 1 normal character
At least 1 capitalized character
At least 1 number 
At least 1 special character.""")
            return
        elif customerID:
            QMessageBox.information(self, "Add Error", "Infornation cannot be entered CustomerID.")
            return
        
        while True:
            customerID = Controller.createCustomerID()
            if not self.ctm.checkExist(customerID):
                break

        self.acc.signUp(username, password, customerID)

        QMessageBox.information(self, "Add Confirmation", "Account has been added successfully.")
        self.clear()

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select a account.")
            return
        
        account = self.getAccount()
        username = account["username"]
        password = account["password"]
        
        if not Controller.checkPassword(password):
            QMessageBox.information(self, "Sign up fail", """Please enter the password with: 
At least 6 characters
At least 1 normal character
At least 1 capitalized character
At least 1 number 
At least 1 special character.""")
            return

        self.acc.update(username, password)
        self.search()

    def search(self):
        account = self.getAccount()
        accountResult = self.acc.search(username=account["username"],
                                    password=account["password"],
                                    customerID=account["customerID"],
        )
        self.showData(accountResult)
    
    def showData(self, accountResult):
        self.ui.table.setRowCount(0)
        if accountResult:
            self.ui.table.setRowCount(len(accountResult))

            for row, info in enumerate(accountResult):
                infoList = [
                    info["username"],
                    info["password"],
                    info["customerID"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getAccount(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        customerID = self.ui.customerID.text().strip()

        account = {
            "username": username,
            "password": password,
            "customerID": customerID
        }

        return account

    def clear(self):
        self.selectRow = -1
        self.ui.username.clear()
        self.ui.password.clear()
        self.ui.customerID.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select a account.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        account = self.getAccount()
        username = account["username"]
        self.acc.delete(username)
        QMessageBox.information(self, "Delete Confirmation", "Account has been deleted successfully.")
        self.clear()
