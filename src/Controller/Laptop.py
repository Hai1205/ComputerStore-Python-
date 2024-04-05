from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.Laptop import Ui_Laptop

from Model.Model_ProductDetail import Model_ProductDetail

class Laptop(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_Laptop()
        self.ui.setupUi(self)

        self.pdd = Model_ProductDetail()
        
        self.Product = None

        self.button()
    
    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.account.clicked.connect(self.account)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.employee.clicked.connect(self.employee)
        self.ui.customer.clicked.connect(self.customer)

        self.ui.back.clicked.connect(self.back)
        self.ui.add.clicked.connect(self.add)
        self.ui.update.clicked.connect(self.update)
        self.ui.clear.clicked.connect(self.clear)
    
    def setProduct(self, product):
        self.Product = product
    
    def management(self):
        self.general.showProductAdmin()
        self.general.page(7)

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
    
    def customer(self):
        self.general.showCustomerAdmin()
        self.general.page(4)

    def back(self):
        self.general.showProductAdmin()
        self.general.page(7)
    
    def getDetail(self):
        productID = self.product["productID"]
        MFG = self.ui.MFG.text().strip()
        RAM = self.ui.RAM.text().strip()
        ROM = self.ui.ROM.text().strip()
        CPU = self.ui.CPU.text().strip()
        VGA = self.ui.VGA.text().strip()
        keyboard = self.ui.keyboard.text().strip()
        screen = self.ui.screen.text().strip()
        OS = self.ui.OS.text().strip()
        size = self.ui.size.text().strip()
        pin = self.ui.pin.text().strip()
        type = self.ui.type.currentText().strip()

        detail = {
            "productID": productID,
            "MFG": MFG,
            "RAM": RAM,
            "ROM": ROM,
            "CPU": CPU,
            "keyboard": keyboard,
            "screen": screen,
            "VGA": VGA,
            "OS": OS,
            "size": size,
            "pin": pin,
            "type": type
        }

        return detail

    def add(self):
        detail = self.getDetail()
        self.pdd.addLaptop(detail["productID"], detail["MFG"], detail["RAM"], detail["ROM"], detail["CPU"], detail["VGA"], detail["keyboard"], detail["screen"], detail["OS"], detail["size"], detail["pin"], detail["type"])
        QMessageBox.information(self, "Add Confirmation", "Product has been added successfully.")

    def update(self):
        detail = self.getDetail()
        self.pdd.updateLaptop(detail["productID"], detail["MFG"], detail["RAM"], detail["ROM"], detail["CPU"], detail["VGA"], detail["keyboard"], detail["screen"], detail["OS"], detail["size"], detail["pin"], detail["type"])

    def clear(self):
        self.ui.MFG.clear()
        self.ui.RAM.clear()
        self.ui.ROM.clear()
        self.ui.CPU.clear()
        self.ui.VGA.clear()
        self.ui.keyboard.clear()
        self.ui.screen.clear()
        self.ui.OS.clear()
        self.ui.size.clear()
        self.ui.pin.clear()
        self.ui.type.setCurrentIndex(0)
    
    def showData(self):
        detail = self.getDetail()
        self.ui.MFG.setText(detail["MFG"])
        self.ui.RAM.setText(detail["RAM"])
        self.ui.size.setText(detail["size"])
        self.ui.ROM.setText(detail["ROM"])
        self.ui.CPU.setText(detail["CPU"])
        self.ui.VGA.setText(detail["VGA"])
        self.ui.keyboard.setText(detail["keyboard"])
        self.ui.screen.setText(detail["screen"])
        self.ui.OS.setText(detail["OS"])
        self.ui.pin.setText(detail["pin"])
        self.ui.type.setCurrentText(detail["type"])