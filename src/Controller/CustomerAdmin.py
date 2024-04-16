from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from View.CustomerAdmin import Ui_CustomerAdmin

from Model.Model_Customer import Model_Customer

from Controller.Controller import Controller

class CustomerAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_CustomerAdmin()
        self.ui.setupUi(self)

        self.ctm = Model_Customer()

        self.button()
        self.clear()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.product.clicked.connect(self.product)
        self.ui.account.clicked.connect(self.account)
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

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

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
        self.ui.customerID.setEnabled(bool)
        self.ui.add.setEnabled(bool)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a customer.")
            return
        
        self.setEnabled(False)
        customerID = self.ui.table.item(self.selectRow, 0).text().strip()
        firstname = self.ui.table.item(self.selectRow, 1).text().strip()
        lastname = self.ui.table.item(self.selectRow, 2).text().strip()
        address = self.ui.table.item(self.selectRow, 3).text().strip()
        phone = self.ui.table.item(self.selectRow, 4).text().strip()

        self.ui.customerID.setText(customerID)
        self.ui.firstname.setText(firstname)
        self.ui.lastname.setText(lastname)
        self.ui.address.setText(address)
        self.ui.phone.setText(phone)

    def add(self):
        customer = self.getCustomer()
        customerID = customer["customerID"]
        firstname = customer["firstname"]
        lastname = customer["lastname"]
        address = customer["address"]
        phone = customer["phone"]

        if customerID:
            QMessageBox.information(self, "Add Error", "Infornation cannot be entered customerID.")
            return
        elif not firstname:
            QMessageBox.information(self, "Add Error", "Firstname can not be blank.")
            return
        elif not lastname:
            QMessageBox.information(self, "Add Error", "Lastname can not be blank.")
            return
        elif not address:
            QMessageBox.information(self, "Add Error", "Address can not be blank.")
            return
        elif not phone:
            QMessageBox.information(self, "Add Error", "Phone time can not be blank.")
            return
        elif not Controller.checkPhone(phone):
            QMessageBox.information(self, "Sign up fail", "Please enter the correct phone number format.")
            return
        
        while True:
            customerID = Controller.createCustomerID()
            if not self.ctm.checkExist(customerID):
                break

        self.ctm.add(customerID, firstname, lastname, address, phone)

        QMessageBox.information(self, "Add Confirmation", "Customer has been added successfully.")
        self.clear()

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select your import.")
            return
        
        customer = self.getCustomer()
        customerID = customer["customerID"]
        firstname = customer["firstname"]
        lastname = customer["lastname"]
        address = customer["address"]
        phone = customer["phone"]

        if not Controller.checkPhone(phone):
            QMessageBox.information(self, "Update Error", "Please enter the correct phone number format.")
            return

        self.ctm.update(customerID, firstname, lastname, address, phone)
        self.search()

    def search(self):
        customer = self.getCustomer()
        customerResult = self.ctm.search(customerID=customer["customerID"],
                                    firstname=customer["firstname"],
                                    lastname=customer["lastname"],
                                    address=customer["address"],
                                    phone=customer["phone"],
        )
        self.showData(customerResult)
    
    def showData(self, customerResult):
        self.ui.table.setRowCount(0)
        if customerResult:
            self.ui.table.setRowCount(len(customerResult))

            for row, info in enumerate(customerResult):
                infoList = [
                    info["customerID"],
                    info["firstname"],
                    info["lastname"],
                    info["address"],
                    info["phone"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getCustomer(self):
        customerID = self.ui.customerID.text().strip()
        firstname = self.ui.firstname.text().strip()
        lastname = self.ui.lastname.text().strip()
        address = self.ui.address.text().strip()
        phone = self.ui.phone.text().strip()

        customer = {
            "customerID": customerID,
            "firstname": firstname,
            "lastname": lastname,
            "address": address,
            "phone": phone
        }

        return customer

    def clear(self):
        self.selectRow = -1
        self.ui.customerID.clear()
        self.ui.firstname.clear()
        self.ui.lastname.clear()
        self.ui.address.clear()
        self.ui.phone.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select the customer.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        customer = self.getCustomer()
        customerID = customer["customerID"]
        self.ctm.delete(customerID)
        QMessageBox.information(self, "Delete Confirmation", "Customer has been deleted successfully.")
        self.clear()
