import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from Controller.SignIn import SignIn
from Controller.SignUp import SignUp

from Controller.AccountAdmin import AccountAdmin
from Controller.WarrantyAdmin import WarrantyAdmin
from Controller.CustomerAdmin import CustomerAdmin
from Controller.EmployeeAdmin import EmployeeAdmin
from Controller.ImportAdmin import ImportAdmin
from Controller.ProductAdmin import ProductAdmin
from Controller.SupplierAdmin import SupplierAdmin
from Controller.InvoiceAdmin import InvoiceAdmin

from Controller.CartUser import CartUser
from Controller.ProductUser import ProductUser
from Controller.SettingUser import SettingUser
from Controller.WarrantyUser import WarrantyUser

from Controller.RAM import RAM
from Controller.CPU import CPU
from Controller.VGA import VGA
from Controller.Keyboard import Keyboard
from Controller.Screen import Screen
from Controller.Laptop import Laptop
from Controller.ROM import ROM

from Controller.ProductDetail import ProductDetail
from Controller.InvoiceDetail import InvoiceDetail
from Controller.ImportDetail import ImportDetail

from Controller.SalesByYears import SalesByYears
from Controller.SalesByEmployees import SalesByEmployees
from Controller.SalesByProducts import SalesByProducts
from Controller.SpendsByYears import SpendsByYears
from Controller.SpendsBySuppliers import SpendsBySuppliers
from Controller.SpendsByProducts import SpendsByProducts
class General(QMainWindow):
    def __init__(self, app = QApplication(sys.argv)):
        super().__init__()
        self.app = app
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setFixedSize(1163, 768)

        self.SignIn = SignIn(self) #0
        self.stacked_widget.addWidget(self.SignIn)

        self.SignUp = SignUp(self) #1
        self.stacked_widget.addWidget(self.SignUp)

        self.AccountAdmin = AccountAdmin(self) #2
        self.stacked_widget.addWidget(self.AccountAdmin)

        self.WarrantyAdmin = WarrantyAdmin(self) #3
        self.stacked_widget.addWidget(self.WarrantyAdmin)

        self.CustomerAdmin = CustomerAdmin(self) #4
        self.stacked_widget.addWidget(self.CustomerAdmin)

        self.EmployeeAdmin = EmployeeAdmin(self) #5
        self.stacked_widget.addWidget(self.EmployeeAdmin)

        self.ImportAdmin = ImportAdmin(self) #6
        self.stacked_widget.addWidget(self.ImportAdmin)

        self.ProductAdmin = ProductAdmin(self) #7
        self.stacked_widget.addWidget(self.ProductAdmin)

        self.SupplierAdmin = SupplierAdmin(self) #8
        self.stacked_widget.addWidget(self.SupplierAdmin)

        self.InvoiceAdmin = InvoiceAdmin(self) #9
        self.stacked_widget.addWidget(self.InvoiceAdmin)

        self.CartUser = CartUser(self) #10
        self.stacked_widget.addWidget(self.CartUser)

        self.ProductUser = ProductUser(self) #11
        self.stacked_widget.addWidget(self.ProductUser)

        self.SettingUser = SettingUser(self) #12
        self.stacked_widget.addWidget(self.SettingUser)

        self.WarrantyUser = WarrantyUser(self) #13
        self.stacked_widget.addWidget(self.WarrantyUser)

        self.RAM = RAM(self) #14
        self.stacked_widget.addWidget(self.RAM)

        self.ROM = ROM(self) #15
        self.stacked_widget.addWidget(self.ROM)

        self.Keyboard = Keyboard(self) #16
        self.stacked_widget.addWidget(self.Keyboard)

        self.CPU = CPU(self) #17
        self.stacked_widget.addWidget(self.CPU)

        self.Laptop = Laptop(self) #18
        self.stacked_widget.addWidget(self.Laptop)

        self.VGA = VGA(self) #19
        self.stacked_widget.addWidget(self.VGA)

        self.Screen = Screen(self) #20
        self.stacked_widget.addWidget(self.Screen)

        self.ProductDetail = ProductDetail(self) #21
        self.stacked_widget.addWidget(self.ProductDetail)

        self.InvoiceDetail = InvoiceDetail(self) #22
        self.stacked_widget.addWidget(self.InvoiceDetail)

        self.ImportDetail = ImportDetail(self) #23
        self.stacked_widget.addWidget(self.ImportDetail)

        self.SalesByYears = SalesByYears(self) #24
        self.stacked_widget.addWidget(self.SalesByYears)
        
        self.SalesByEmployees = SalesByEmployees(self) #25
        self.stacked_widget.addWidget(self.SalesByEmployees)

        self.SalesByProducts = SalesByProducts(self) #26
        self.stacked_widget.addWidget(self.SalesByProducts)

        self.SpendsByYears = SpendsByYears(self) #27
        self.stacked_widget.addWidget(self.SpendsByYears)

        self.SpendsBySuppliers = SpendsBySuppliers(self) #28
        self.stacked_widget.addWidget(self.SpendsBySuppliers)

        self.SpendsByProducts = SpendsByProducts(self) #29
        self.stacked_widget.addWidget(self.SpendsByProducts)

        self.page(0)
        self.stacked_widget.show()
        sys.exit(self.app.exec())

    def setCustomerID(self, customerID):
        if customerID == "admin": 
            self.ProductAdmin.setCustomerID(customerID)
            self.WarrantyAdmin.setCustomerID(customerID)
            self.InvoiceDetail.setCustomerID(customerID)
        else:
            self.ProductUser.setCustomerID(customerID)
            self.WarrantyUser.setCustomerID(customerID)
            self.CartUser.setCustomerID(customerID)
            self.SettingUser.setCustomerID(customerID)
        self.ProductDetail.setCustomerID(customerID)

    def page(self, index):
        self.stacked_widget.setCurrentIndex(index)
    
    def detail(self, product):
        self.ProductDetail.setProduct(product)
        self.Laptop.setProduct(product)
        self.RAM.setProduct(product)
        self.ROM.setProduct(product)
        self.CPU.setProduct(product)
        self.VGA.setProduct(product)
        self.Keyboard.setProduct(product)
        self.Screen.setProduct(product)
        self.showProductDetail()

    def importDetail(self, Import):
        self.ImportDetail.setImport(Import)
        self.showImportDetail()

    def invoiceDetail(self, invoice):
        self.InvoiceDetail.setInvoice(invoice)
        self.showInvoiceDetail()
    
    def showProductAdmin(self):
        self.ProductAdmin.clear()

    def showAccountAdmin(self):
        self.AccountAdmin.clear()

    def showWarrantyAdmin(self):
        self.WarrantyAdmin.clear()

    def showProductAdmin(self):
        self.ProductAdmin.clear()

    def showCustomerAdmin(self):
        self.CustomerAdmin.clear()

    def showEmployeeAdmin(self):
        self.EmployeeAdmin.clear()

    def showImportAdmin(self):
        self.ImportAdmin.clear()

    def showProductAdmin(self):
        self.ProductAdmin.clear()

    def showSupplierAdmin(self):
        self.SupplierAdmin.clear()

    def showInvoiceAdmin(self):
        self.InvoiceAdmin.clear()

    def showCartUser(self):
        self.CartUser.clear()

    def showProductUser(self):
        self.ProductUser.clear()

    def showSettingUser(self):
        self.SettingUser.clear()

    def showWarrantyUser(self):
        self.WarrantyUser.clear()

    def showRAM(self):
        self.RAM.showData()
    
    def showROM(self):
        self.ROM.showData()
    
    def showKeyboard(self):
        self.Keyboard.showData()

    def showCPU(self):
        self.CPU.showData()
    
    def showLaptop(self):
        self.Laptop.showData()
    
    def showVGA(self):
        self.VGA.showData()
    
    def showScreen(self):
        self.Screen.showData()
    
    def showProductDetail(self):
        self.ProductDetail.showData()
    
    def showInvoiceDetail(self):
        self.InvoiceDetail.showData()
    
    def showImportDetail(self):
        self.ImportDetail.showData()
