from PyQt6.QtWidgets import QMainWindow
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
            self.ui.massage.setText("Username can not be blank.")
            return
        elif not password:
            self.ui.massage.setText("Password can not be blank.")
            return
        elif not rePassword:
            self.ui.massage.setText("RePassword can not be blank.")
            return
        elif not firstname:
            self.ui.massage.setText("Firstname can not be blank.")
            return
        elif not lastname:
            self.ui.massage.setText("Lastname can not be blank.")
            return
        elif not address:
            self.ui.massage.setText("Address can not be blank.")
            return
        elif not phone:
            self.ui.massage.setText("Phone can not be blank.")
            return
        elif password != rePassword:
            self.ui.massage.setText("Password and Repassword do not match.")
            return
        elif self.acc.checkExist(username):
            self.ui.massage.setText("Username already exists")
            return
        
        try:
            self.acc.signUp(username, password, customerID)
            self.ctm.add(customerID, firstname, lastname, address, phone)
        
        except Exception as e:
            print(e)

        self.ui.username.clear()
        self.ui.password.clear()
        self.ui.rePassword.clear()
        self.ui.firstname.clear()
        self.ui.lastname.clear()
        self.ui.address.clear()
        self.ui.phone.clear()

        self.ui.massage.setText("Successful.")