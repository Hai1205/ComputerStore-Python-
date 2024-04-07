from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from View.SpendsBySuppliers import Ui_SpendsBySuppliers

class SpendsBySuppliers(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_SpendsBySuppliers()
        self.ui.setupUi(self)

        self.button()

    def button(self):
        self.ui.management.clicked.connect(self.management)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.salesByYears.clicked.connect(self.salesByYears)
        self.ui.salesByEmployees.clicked.connect(self.salesByEmployees)
        self.ui.salesByProducts.clicked.connect(self.salesByProducts)
        self.ui.spendsByYears.clicked.connect(self.spendsByYears)
        self.ui.spendsByProducts.clicked.connect(self.spendsByProducts)

    def management(self):
        self.general.showProductAdmin()
        self.general.page(7)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)
    
    def salesByYears(self):
        # self.general.showProductAdmin()
        self.general.page(24)

    def salesByEmployees(self):
        # self.general.showImportAdmin()
        self.general.page(25)

    def salesByProducts(self):
        # self.general.showCustomerAdmin()
        self.general.page(26)

    def spendsByYears(self):
        # self.general.showSupplierAdmin()
        self.general.page(27)

    def spendsByProducts(self):
        # self.general.showInvoiceAdmin()
        self.general.page(29)