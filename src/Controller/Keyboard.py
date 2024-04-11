from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.Keyboard import Ui_Keyboard

from Model.Model_ProductDetail import Model_ProductDetail

class Keyboard(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_Keyboard()
        self.ui.setupUi(self)
        
        self.pdd = Model_ProductDetail()
        
        self.productID = None

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
    
    def setProductID(self, productID):
        self.productID = productID
    
    def management(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def statistic(self):
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
    
    def customer(self):
        self.general.showCustomerAdmin()
        self.general.page(4)

    def back(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def getDetail(self):
        result = self.pdd.search(self.productID)

        MFG = result[0]["MFG"]
        layout = result[0]["layout"]
        LED = result[0]["LED"]
        keycap = result[0]["keycap"]
        size = result[0]["size"]
        switch = result[0]["switch"]
        pin = result[0]["pin"]
        hotswap = result[0]["hotswap"]

        detail = {
            "productID": self.productID,
            "MFG": MFG,
            "size": size,
            "layout": layout,
            "LED": LED,
            "keycap": keycap,
            "switch": switch,
            "pin": pin,
            "hotswap": hotswap
        }

        return detail

    def add(self):
        detail = self.getDetail()
        self.pdd.addKeyboard(detail["productID"], detail["MFG"], detail["layout"], detail["size"], detail["LED"], detail["keycap"], detail["switch"], detail["pin"], detail["hotswap"])
        QMessageBox.information(self, "Add Confirmation", "productID has been added successfully.")

    def update(self):
        detail = self.getDetail()
        self.pdd.updateKeyboard(detail["productID"], detail["MFG"], detail["layout"], detail["size"], detail["LED"], detail["keycap"], detail["switch"], detail["pin"], detail["hotswap"])

    def clear(self):
        self.ui.MFG.clear()
        self.ui.layout.clear()
        self.ui.size_2.clear()
        self.ui.LED.clear()
        self.ui.keycap.clear()
        self.ui.switch_2.clear()
        self.ui.pin.clear()
        self.ui.hotswap.currentIndex(0)
    
    def showData(self):
        detail = self.getDetail()
        self.ui.MFG.setText(detail["MFG"])
        self.ui.layout.setText(detail["layout"])
        self.ui.size_2.setText(detail["size_2"])
        self.ui.LED.setText(detail["LED"])
        self.ui.keycap.setText(detail["keycap"])
        self.ui.switch_2.setText(detail["switch_2"])
        self.ui.pin.setText(detail["pin"])
        self.ui.hotswap.setCurrentText(detail["hotswap"])