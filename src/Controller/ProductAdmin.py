from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime, timedelta

from View.ProductAdmin import Ui_ProductAdmin

from Model.Model_Product import Model_Product
from Model.Model_ProductDetail import Model_ProductDetail
from Model.Model_Warranty import Model_Warranty
from Model.Model_Employee import Model_Employee
from Model.Model_Import import Model_Import
from Model.Model_ImportDetail import Model_ImportDetail
from Model.Model_Invoice import Model_Invoice
from Model.Model_InvoiceDetail import Model_InvoiceDetail
from Model.Model_Supplier import Model_Supplier

from Controller.Controller import Controller
from Controller.SupplierAdmin import SupplierAdmin

class ProductAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_ProductAdmin()
        self.ui.setupUi(self)

        self.pd = Model_Product()
        self.pdd = Model_ProductDetail()
        self.ip = Model_Import()
        self.wrt = Model_Warranty()
        self.ep = Model_Employee()
        self.ipd = Model_ImportDetail()
        self.iv = Model_Invoice()
        self.ivd = Model_InvoiceDetail()
        self.sp = Model_Supplier()
        self.csp = SupplierAdmin()

        self.button()
        self.updateCombobox()

        self.purchaseDate = datetime.now()
        self.selectRow = -1
        self.ui.type.setCurrentIndex(0)
        self.ui.supplierName.setCurrentIndex(0)
        self.employeeID = None
        self.importID = None
        self.invoiceID = None
        self.totalCost = 0
    
    def updateCombobox(self):
        self.ui.supplierName.clear()
        supplierList = self.csp.updateCombobox()
        self.ui.supplierName.addItems(supplierList)

    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.account.clicked.connect(self.account)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.employee.clicked.connect(self.employee)

        self.ui.select.clicked.connect(self.select)
        self.ui.detail.clicked.connect(self.detail)
        self.ui.add.clicked.connect(self.add)
        self.ui.sell.clicked.connect(self.sell)
        self.ui.update.clicked.connect(self.update)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)

    def setCustomerID(self, customerID):
        self.customerID = customerID

    def statistic(self):
        self.general.page(24)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

    def import_2(self):
        self.general.showImportAdmin()
        self.general.page(6)

    def customer(self):
        self.general.showCustomerAdmin()
        self.general.page(4)

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
        self.ui.productID.setEnabled(bool)
        self.ui.supplierName.setEnabled(bool)
        self.ui.productName.setEnabled(bool)
        self.ui.type.setEnabled(bool)
    
    def select(self):
        self.setEnabled(False)
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow != -1:
            productID = self.ui.table.item(self.selectRow, 0).text().strip()
            supplierName = self.ui.table.item(self.selectRow, 1).text().strip()
            productName = self.ui.table.item(self.selectRow, 2).text().strip()
            type = self.ui.table.item(self.selectRow, 3).text().strip()
            quantity = self.ui.table.item(self.selectRow, 4).text().strip()
            warrantyTime = self.ui.table.item(self.selectRow, 5).text().strip()
            price = self.ui.table.item(self.selectRow, 6).text().strip()

            self.ui.productID.setText(productID)
            self.ui.supplierName.setCurrentText(supplierName)
            self.ui.productName.setText(productName)
            self.ui.quantity.setText(quantity)
            self.ui.price.setText(price)
            self.ui.type.setCurrentText(type)
            self.ui.warrantyTime.setText(warrantyTime)
        
    def detail(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Error", "Please select the product.")
            return
        
        # self.general.detail(product=self.getProduct())
        # self.general.page(21)
        product = self.getProduct()
        type = product["type"]
        if type == "Laptop":
            self.general.showLaptop()
            self.general.page(18)
        elif type == "RAM":
            self.general.showRAM()
            self.general.page(14)
        elif type == "ROM":
            self.general.showROM()
            self.general.page(15)
        elif type == "CPU":
            self.general.showCPU()
            self.general.page(17)
        elif type == "VGA":
            self.general.showVGA()
            self.general.page(19)
        elif type == "Keyboard":
            self.general.showKeyboard()
            self.general.page(16)
        elif type == "Screen":
            self.general.showScreen()
            self.general.page(20)

    def add(self):
        if self.employeeID is None:
            employeeID = self.ep.selectRandom()
            self.employeeID = employeeID["employeeID"]
        if self.importID is None:
            while True:
                self.importID = Controller.createImportID()
                if not self.iv.checkExist(self.importID):
                    break

        product = self.getProduct()
        productID = product["productID"]
        supplierName = product["supplierName"]
        productName = product["productName"]
        type = product["type"]
        quantity = int(product["quantity"])
        warrantyTime = int(product["warrantyTime"])
        price = int(product["price"])
        cost = quantity * price
        self.totalCost += cost
        if productID == "":
            while True:
                productID = Controller.createProductID()
                if not self.pd.checkExist(productID):
                    break

        if supplierName == "All":
            QMessageBox.information(self, "Import Error", "Please choose a different supplier name than All.")
            return 
        if type == "All":
            QMessageBox.information(self, "Import Error", "Please choose a different type than All.")
            return
        if not self.ip.checkExist(self.importID):
            self.ip.add(self.importID, self.employeeID, supplierName, self.purchaseDate.date(), self.totalCost)
        self.ipd.add(self.importID, productID, quantity, price, cost)
        self.ip.update(self.importID, self.purchaseDate, self.totalCost)

        if self.pd.checkExist(productID):
            self.pd.increaseQuantity(productID, quantity, price)
            QMessageBox.information(self, "Add Confirmation", "Product has been added successfully.")
        else:
            self.general.detail(product)
            self.pd.add(productID, supplierName, productName, type, quantity, warrantyTime, price)
            
            if type == "Laptop":
                self.general.page(18)
            elif type == "RAM":
                self.general.page(14)
            elif type == "ROM":
                self.general.page(15)
            elif type == "CPU":
                self.general.page(17)
            elif type == "VGA":
                self.general.page(19)
            elif type == "Keyboard":
                self.general.page(16)
            elif type == "Screen":
                self.general.page(20)

        self.clear()
    
    def sell(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Sell Error", "Please select the product.")
            return
        
        warrantyID = None
        while True:
            warrantyID = Controller.createWarrantyID()
            if not self.wrt.checkExist(warrantyID):
                break
        if self.employeeID is None:
            employeeID = self.ep.selectRandom()
            self.employeeID = employeeID["employeeID"]
        if self.invoiceID is None:
            while True:
                self.invoiceID = Controller.createInvoiceID()
                if not self.iv.checkExist(self.invoiceID):
                    break

        product = self.getProduct()
        productID = product["productID"]
        customerID = product["customerID"]
        quantity = int(product["quantity"])
        warrantyTime = int(product["warrantyTime"])
        price = int(product["price"])
        cost = quantity * price
        newDate = self.purchaseDate + timedelta(days=warrantyTime*30+10)
        EXP = newDate.date()
        self.totalCost += cost

        if not self.iv.checkExist(self.invoiceID):
            self.iv.add(self.invoiceID, self.employeeID, customerID, self.purchaseDate.date(), self.totalCost)
        self.ivd.add(self.invoiceID, productID, warrantyID, quantity, price, cost)
        self.wrt.add(warrantyID, productID, self.invoiceID, customerID, self.purchaseDate.date(), warrantyTime, EXP)
        self.iv.update(self.invoiceID, self.purchaseDate, self.totalCost)
        self.pd.decreaseQuantity(productID, quantity)

        QMessageBox.information(self, "Sell Confirmation", "Sell has been placed successfully.")
        self.clear()

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select the product.")
            return
        
        product = self.getProduct()
        productID = product["productID"]
        productName = product["productName"]
        warrantyTime = int(product["warrantyTime"])
        price = int(product["price"])

        self.pd.update(productID, productName, warrantyTime, price)
        self.search()

    def search(self):
        product = self.getProduct()
        supplierName = product["supplierName"]
        if supplierName == "All":
            supplierName = None
        type = product["type"]
        if type == "All":
            type = None
        productResult = self.pd.search(productID=product["productID"],
                                    supplierName=supplierName,
                                    productName=product["productName"],
                                    type=type,
                                    quantity=product["quantity"],
                                    warrantyTime=product["warrantyTime"],
                                    price=product["price"]
        )
        self.showData(productResult)

    def clear(self):
        self.ui.productID.clear()
        self.ui.supplierName.setCurrentIndex(0)
        self.ui.customerID.clear()
        self.ui.productName.clear()
        self.ui.quantity.clear()
        self.ui.price.clear()
        self.ui.type.setCurrentIndex(0)
        self.ui.warrantyTime.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select the product.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        product = self.getProduct()
        productID = product["productID"]
        self.pd.delete(productID)
        self.pdd.delete(productID)
        QMessageBox.information(self, "Delete Confirmation", "Product has been deleted successfully.")
        self.clear()

    def showData(self, productResult):
        self.ui.table.setRowCount(0)
        if productResult:
            self.ui.table.setRowCount(len(productResult))

            for row, info in enumerate(productResult):
                infoList = [
                    info["productID"],
                    info["supplierName"],
                    info["productName"],
                    info["type"],
                    info["quantity"],
                    info["warrantyTime"],
                    info["price"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getProduct(self):
        productID = self.ui.productID.text().strip()
        customerID = self.ui.customerID.text().strip()
        supplierName = self.ui.supplierName.currentText().strip()
        productName = self.ui.productName.text().strip()
        type = self.ui.type.currentText().strip()
        quantity = self.ui.quantity.text().strip()
        warrantyTime = self.ui.warrantyTime.text().strip()
        price = self.ui.price.text().strip()

        product = {
            "productID": productID,
            "customerID": customerID,
            "supplierName": supplierName,
            "productName": productName,
            "type": type,
            "warrantyTime": warrantyTime,
            "price": price,
            "quantity": quantity
        }

        return product
