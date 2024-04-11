from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.SignUp import Ui_SignUp

from Model.Model_Account import Model_Account
from Model.Model_Customer import Model_Customer

from Controller.Controller import Controller

class SignUp(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        self.acc = Model_Account()
        self.ctm = Model_Customer()
        self.button()
    
    def button(self):
        self.ui.signIn.clicked.connect(self.signIn)
        self.ui.signUp.clicked.connect(self.signUp)
    
    def signIn(self):
        self.general.page(0)

    def signUp(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        rePassword = self.ui.rePassword.text().strip()
        firstname = self.ui.firstname.text().strip()
        lastname = self.ui.lastname.text().strip()
        address = self.ui.address.text().strip()
        phone = self.ui.phone.text().strip()

        customerID = None
        while True:
            customerID = Controller.createCustomerID()
            if not self.ctm.checkExist(customerID):
                break

        if not username:
            QMessageBox.information(self, "Sign up fail", "Username can not be blank.")
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
            QMessageBox.information(self, "Sign up fail", "Password can not be blank.")
            return
        elif not Controller.checkPassword(password):
            QMessageBox.information(self, "Sign up fail", """Please enter the password with: 
At least 6 characters
At least 1 normal character
At least 1 capitalized character
At least 1 number 
At least 1 special character.""")
            return
        elif not rePassword:
            QMessageBox.information(self, "Sign up fail", "RePassword can not be blank.")
            return
        elif password != rePassword:
            QMessageBox.information(self, "Sign up fail", "Password and Repassword do not match.")
            return
        elif not firstname:
            QMessageBox.information(self, "Sign up fail", "Firstname can not be blank.")
            return
        elif not lastname:
            QMessageBox.information(self, "Sign up fail", "Lastname can not be blank.")
            return
        elif not address:
            QMessageBox.information(self, "Sign up fail", "Address can not be blank.")
            return
        elif not phone:
            QMessageBox.information(self, "Sign up fail", "Phone can not be blank.")
            return
        elif not Controller.checkPhone(phone):
            QMessageBox.information(self, "Sign up fail", "Please enter the correct phone number format.")
            return
        
        try:
            self.acc.signUp(username, password, customerID)
            self.ctm.add(customerID, firstname, lastname, address, phone)
        
        except Exception as e:
            print(e)

        self.general.page(0)

        self.ui.username.clear()
        self.ui.password.clear()
        self.ui.rePassword.clear()
        self.ui.firstname.clear()
        self.ui.lastname.clear()
        self.ui.address.clear()
        self.ui.phone.clear()

        QMessageBox.information(self, "Sign up fail", "Successful.")