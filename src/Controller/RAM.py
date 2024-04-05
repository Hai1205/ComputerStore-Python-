from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.RAM import Ui_RAM

from Model.Model_ProductDetail import Model_ProductDetail

class RAM(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_RAM()
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
        capacity = self.ui.capacity.text().strip()
        SPDspeed = self.ui.SPDspeed.text().strip()
        CL = self.ui.CL.text().strip()
        size = self.ui.size.text().strip()
        type = self.ui.type.text().strip()

        detail = {
            "productID": productID,
            "MFG": MFG,
            "size": size,
            "capacity": capacity,
            "SPDspeed": SPDspeed,
            "CL": CL,
            "type": type
        }

        return detail

    def add(self):
        detail = self.getDetail()
        self.pdd.addRAM(detail["productID"], detail["MFG"], detail["capacity"], detail["type"], detail["SPDspeed"], detail["CL"], detail["size"])
        QMessageBox.information(self, "Add Confirmation", "Product has been added successfully.")

    def update(self):
        detail = self.getDetail()
        self.pdd.updateRAM(detail["productID"], detail["MFG"], detail["capacity"], detail["type"], detail["SPDspeed"], detail["CL"], detail["size"])

    def clear(self):
        self.ui.MFG.clear()
        self.ui.capacity.clear()
        self.ui.type.clear()
        self.ui.SPDspeed.clear()
        self.ui.CL.clear()
        self.ui.size.clear()
    
    def showData(self):
        detail = self.getDetail()
        self.ui.MFG.setText(detail["MFG"])
        self.ui.capacity.setText(detail["capacity"])
        self.ui.type.setText(detail["type"])
        self.ui.SPDspeed.setText(detail["SPDspeed"])
        self.ui.CL.setText(detail["CL"])
        self.ui.size.setText(detail["size"])