from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from datetime import datetime, timedelta

from View.ProductUser import Ui_ProductUser

from Model.Model_Product import Model_Product
from Model.Model_Warranty import Model_Warranty
from Model.Model_Employee import Model_Employee
from Model.Model_Invoice import Model_Invoice
from Model.Model_InvoiceDetail import Model_InvoiceDetail

from Controller.Controller import Controller
from Controller.SupplierAdmin import SupplierAdmin

class ProductUser(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_ProductUser()
        self.ui.setupUi(self)

        self.pd = Model_Product()
        self.iv = Model_Invoice()
        self.wrt = Model_Warranty()
        self.ep = Model_Employee()
        self.ivd = Model_InvoiceDetail()
        self.csp = SupplierAdmin()

        self.customerID = None
        self.purchaseDate = datetime.now()
        self.selectRow = -1
        self.employeeID = None
        self.invoiceID = None
        self.totalCost = 0

        self.button()
        self.updateCombobox()

    def updateCombobox(self):
        self.ui.supplierName.clear()
        supplierList = self.csp.updateCombobox()
        self.ui.supplierName.addItems(supplierList)     

    def button(self):
        self.ui.cart.clicked.connect(self.cart)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.setting.clicked.connect(self.setting)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.select.clicked.connect(self.select)
        self.ui.order.clicked.connect(self.order)
        self.ui.detail.clicked.connect(self.detail)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
    
    def setCustomerID(self, customerID):
        self.customerID = customerID

    def cart(self):
        self.general.showCartUser()
        self.general.page(10)
    
    def warranty(self):
        self.general.showWarrantyUser()
        self.general.page(13)

    def setting(self):
        self.general.showSettingUser()
        self.general.page(12)
    
    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def select(self):
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow == -1:
            QMessageBox.information(self, "Select Error", "Please select a product.")
            return
            
        self.setEnabled(False)
        productID = self.ui.table.item(self.selectRow, 0).text().strip()
        supplierName = self.ui.table.item(self.selectRow, 1).text().strip()
        productName = self.ui.table.item(self.selectRow, 2).text().strip()
        type = self.ui.table.item(self.selectRow, 3).text().strip()
        warrantyTime = self.ui.table.item(self.selectRow, 5).text().strip()
        price = self.ui.table.item(self.selectRow, 6).text().strip()

        self.ui.productID.setText(productID)
        self.ui.supplierName.setCurrentText(supplierName)
        self.ui.productName.setText(productName)
        self.ui.quantity.setText("1")
        self.ui.price.setText(price)
        self.ui.type.setCurrentText(type)
        self.ui.warrantyTime.setText(warrantyTime)
        
    def setEnabled(self, bool):
        self.ui.productID.setEnabled(bool)
        self.ui.supplierName.setEnabled(bool)
        self.ui.productName.setEnabled(bool)
        self.ui.type.setEnabled(bool)
        self.ui.warrantyTime.setEnabled(bool)
        self.ui.price.setEnabled(bool)

    def detail(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Error", "Please select a product.")
            return
        
        self.general.detailUser(self.getProduct())
        self.general.page(21)

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
        self.ui.productName.clear()
        self.ui.quantity.clear()
        self.ui.price.clear()
        self.ui.type.setCurrentIndex(0)
        self.ui.warrantyTime.clear()
        self.selectRow = -1
        self.search()
        self.setEnabled(True)

    def order(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Order Error", "Please select a product.")
            return

        confirmSignout = QMessageBox.question(self, "Order Confirmation", "Are you sure want to buy this proudct?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.No:
            return
        
        warrantyID = None
        while True:
            warrantyID = Controller.createWarrantyID()
            if not self.wrt.checkExist(warrantyID):
                break
        if self.employeeID is None:
            result = self.ep.selectRandom(position="Sale")
            self.employeeID = result["employeeID"]
        if self.invoiceID is None:
            while True:
                self.invoiceID = Controller.createInvoiceID()
                if not self.iv.checkExist(self.invoiceID):
                    break

        product = self.getProduct()
        productID = product["productID"]
        quantity = product["quantity"]
        warrantyTime = int(product["warrantyTime"])
        price = int(product["price"])

        if not quantity:
            QMessageBox.warning(self, "Warning", "Please enter a value into the quantity.")
            return
        elif not quantity.isdigit():
            QMessageBox.warning(self, "Warning", "Please enter an integer value into the quantity.")
            return

        cost = int(quantity) * price
        newDate = self.purchaseDate + timedelta(days=warrantyTime*30+10)
        EXP = newDate.date()
        self.totalCost += cost

        if not self.iv.checkExist(self.invoiceID):
            self.iv.add(self.invoiceID, self.employeeID, self.customerID, self.purchaseDate.date(), self.totalCost)
        self.ivd.add(self.invoiceID, productID, warrantyID, int(quantity), price, cost)
        self.wrt.add(warrantyID, productID, self.invoiceID, self.customerID, self.purchaseDate, warrantyTime, EXP)
        self.iv.update(self.invoiceID, self.purchaseDate, self.totalCost)
        self.pd.decreaseQuantity(productID, int(quantity))

        QMessageBox.information(self, "Order Confirmation", "Order has been placed successfully.")
        self.search()

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
        supplierName = self.ui.supplierName.currentText().strip()
        productName = self.ui.productName.text().strip()
        type = self.ui.type.currentText().strip()
        quantity = self.ui.quantity.text().strip()
        warrantyTime = self.ui.warrantyTime.text().strip()
        price = self.ui.price.text().strip()

        product = {
            "productID": productID,
            "supplierName": supplierName,
            "productName": productName,
            "type": type,
            "warrantyTime": warrantyTime,
            "price": price,
            "quantity": quantity
        }

        return product
