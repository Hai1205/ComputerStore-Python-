from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.SettingUser import Ui_SettingUser

from Model.Model_Customer import Model_Customer

from Controller.Controller import Controller

class SettingUser(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SettingUser()
        self.ctm = Model_Customer()
        self.ui.setupUi(self)

        self.customerID = None

        self.button()
    
    def setCustomerID(self, customerID):
        self.customerID = customerID

    def button(self):
        self.ui.product.clicked.connect(self.product)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.cart.clicked.connect(self.cart)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.update.clicked.connect(self.update)
        self.ui.clear.clicked.connect(self.clear)

    def product(self):
        self.general.showProductUser()
        self.general.page(11)
    
    def warranty(self):
        self.general.showWarrantyUser()
        self.general.page(13)

    def cart(self):
        self.general.showCartUser()
        self.general.page(10)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def update(self):
        customer = self.getCustomer()
        phone = customer["phone"]
        if not Controller.checkPhone(phone):
            QMessageBox.information(self, "Sign up fail", "Please enter the correct phone number format.")
            return
        self.ctm.update(customerID=self.customerID,
                        firstname=customer["firstname"],
                        lastname=customer["lastname"],
                        address=customer["address"],
                        phone=phone)
        self.showData()
    
    def showData(self):
        customer = self.ctm.search(customerID=self.customerID)
        self.ui.outputCustomerID.setText(self.customerID)
        self.ui.outputFirstname.setText(customer[0]["firstname"])
        self.ui.outputLastname.setText(customer[0]["lastname"])
        self.ui.outputAddress.setText(customer[0]["address"])
        self.ui.outputPhone.setText(customer[0]["phone"])

    def getCustomer(self):
        firstname = self.ui.firstname.text().strip()
        lastname = self.ui.lastname.text().strip()
        address = self.ui.address.text().strip()
        phone = self.ui.phone.text().strip()

        customer = {
            "firstname": firstname,
            "lastname": lastname,
            "address": address,
            "phone": phone,
        }

        return customer

    def clear(self):
        self.ui.firstname.clear()
        self.ui.lastname.clear()
        self.ui.address.clear()
        self.ui.phone.clear()
        self.showData()