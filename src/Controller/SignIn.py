from PyQt6.QtWidgets import QMainWindow, QMessageBox
from View.SignIn import Ui_SignIn
from Model.Model_Account import Model_Account

class SignIn(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SignIn()
        self.ui.setupUi(self)
        self.acc = Model_Account()
        self.button()
    
    def button(self):
        self.ui.signIn.clicked.connect(self.signIn)
        self.ui.signUp.clicked.connect(self.signUp)
    
    def signIn(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        customerID = None
        if not username:
            self.ui.massage.setText("Username can not be blank.")
            return
        elif not password:
            self.ui.massage.setText("Password can not be blank.")
            return
        
        try:
            result = self.acc.signIn(username, password)

            if result is not None:
                customerID = result["customerID"]
                self.general.setCustomerID(customerID)
                self.ui.massage.setText("")
            else:
                self.ui.massage.setText("Username or password is incorrect.")
                return

        except Exception as e:
            print(e)

        self.clear()

        if customerID == "admin":
            self.general.showProductAdmin()
            self.general.page(7)
        else:
            self.general.showProductUser()
            self.general.page(11)
        
    def clear(self):
        self.ui.username.clear()
        self.ui.password.clear()

    def signUp(self):
        self.clear()
        self.general.page(1)