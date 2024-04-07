from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate
from datetime import datetime, timedelta

from View.WarrantyUser import Ui_WarrantyUser

from Model.Model_Warranty import Model_Warranty

from Controller.Controller import Controller

class WarrantyUser(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_WarrantyUser()
        self.ui.setupUi(self)

        self.wrt = Model_Warranty()

        self.customerID = None
        self.ui.purchaseDate.setDisplayFormat("yyyy-MM-dd")
        self.ui.purchaseDate.setDate(QDate.currentDate())
        self.ui.EXP.setDisplayFormat("yyyy-MM-dd")
        EXP = datetime.now() + timedelta(days=24*30+10)
        self.ui.EXP.setDate(EXP.date())

        self.button()
        self.clear()
    
    def setCustomerID(self, customerID):
        self.customerID = customerID

    def button(self):
        self.ui.product.clicked.connect(self.product)
        self.ui.cart.clicked.connect(self.cart)
        self.ui.setting.clicked.connect(self.setting)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.expiryList.clicked.connect(self.expiryList)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)

    def product(self):
        self.general.page(11)
    
    def cart(self):
        self.general.page(10)

    def setting(self):
        self.general.page(12)

    def signOut(self):
        confirmSignout = QMessageBox.question(self, "Sign out", "Are you sure want to sign out?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmSignout == QMessageBox.StandardButton.Yes:
            self.general.page(0)

    def expiryList(self):
        warranty = self.getWarranty()

        purchaseDate = warranty["purchaseDate"]
        if Controller.compare_dates(datetime.strptime(purchaseDate, "%Y-%m-%d").date(), datetime(2000, 1, 1).date()):
            purchaseDate = None
        EXP = warranty["EXP"]
        if Controller.compare_dates(datetime.strptime(EXP, "%Y-%m-%d").date(), datetime(2000, 1, 1).date()):
            EXP = None

        warrrantyResult = self.wrt.expiryList(warrantyID=warranty["warrantyID"],
                                        productID=warranty["productID"],
                                        invoiceID=warranty["invoiceID"],
                                        customerID=self.customerID,
                                        purchaseDate=purchaseDate,
                                        warrantyTime=warranty["warrantyTime"],
                                        EXP=EXP
        )
        self.showData(warrrantyResult)

    def showData(self, warrrantyResult):
        self.ui.table.setRowCount(0)
        if warrrantyResult:
            self.ui.table.setRowCount(len(warrrantyResult))

            for row, info in enumerate(warrrantyResult):
                infoList = [
                    info["warrantyID"],
                    info["productID"],
                    info["invoiceID"],
                    info["purchaseDate"],
                    info["warrantyTime"],
                    info["EXP"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getWarranty(self):
        warrantyID = self.ui.warrantyID.text().strip()
        productID = self.ui.productID.text().strip()
        invoiceID = self.ui.invoiceID.text().strip()
        purchaseDate = self.ui.purchaseDate.text().strip()
        warrantyTime = self.ui.warrantyTime.text().strip()
        EXP = self.ui.EXP.text().strip()

        warranty = {
            "warrantyID": warrantyID,
            "productID": productID,
            "invoiceID": invoiceID,
            "purchaseDate": purchaseDate,
            "warrantyTime": warrantyTime,
            "EXP": EXP
        }

        return warranty

    def search(self):
        warranty = self.getWarranty()

        warrrantyResult = self.wrt.search(warrantyID=warranty["warrantyID"],
                                        productID=warranty["productID"],
                                        invoiceID=warranty["invoiceID"],
                                        customerID=self.customerID,
                                        purchaseDate=warranty["purchaseDate"],
                                        warrantyTime=warranty["warrantyTime"],
                                        EXP=warranty["EXP"]
        )
        self.showData(warrrantyResult)

    def clear(self):
        self.ui.warrantyID.clear()
        self.ui.productID.clear()
        self.ui.invoiceID.clear()
        self.ui.warrantyTime.clear()
        self.search()