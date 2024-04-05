from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from View.InvoiceDetail import Ui_InvoiceDetail

from Model.Model_InvoiceDetail import Model_InvoiceDetail

class InvoiceDetail(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_InvoiceDetail()
        self.ui.setupUi(self)
        
        self.ivd = Model_InvoiceDetail()
        
        self.invoice = None
        self.customerID = None

        self.button()

    def setInvoice(self, invoice):
        self.invoice = invoice
    
    def setCustomerID(self, customerID):
        self.customerID = customerID
    
    def button(self):
        self.ui.back.clicked.connect(self.back)
    
    def back(self):
        if self.customerID == "admin":
            self.general.page(9)
        else:
            self.general.page(10)
    
    def showData(self):
        invoiceID = self.invoice["invoiceID"]
        employeeID = self.invoice["employeeID"]
        customerID = self.invoice["customerID"]
        purchaseDate = self.invoice["date"]
        totalCost = self.invoice["totalCost"]

        self.ui.invoiceID.setText(invoiceID)
        self.ui.employeeID.setText(employeeID)
        self.ui.customerID.setText(customerID)
        self.ui.purchaseDate.setText(purchaseDate)
        self.ui.totalCost.setText(totalCost)

        invoiceResult = self.ivd.search(invoiceID=invoiceID, customerID=self.customerID)
        self.ui.table.setRowCount(0)
        if invoiceResult:
            self.ui.table.setRowCount(len(invoiceResult))

            for row, info in enumerate(invoiceResult):
                infoList = [
                    info["productID"],
                    info["warrantyID"],
                    info["quantity"],
                    info["price"],
                    info["cost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return