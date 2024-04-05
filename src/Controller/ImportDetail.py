from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from View.ImportDetail import Ui_ImportDetail

from Model.Model_ImportDetail import Model_ImportDetail

class ImportDetail(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_ImportDetail()
        self.ui.setupUi(self)

        self.ipd = Model_ImportDetail()
        
        self.Import = None

        self.button()
    
    def setImport(self, Import):
        self.Import = Import
    
    def button(self):
        self.ui.back.clicked.connect(self.back)
    
    def back(self):
        self.general.page(6)
    
    def showData(self):
        importID = self.Import["importID"]
        employeeID = self.Import["employeeID"]
        supplierID = self.Import["supplierID"]
        purchaseDate = self.Import["date"]
        totalCost = self.Import["totalCost"]

        self.ui.importID.setText(importID)
        self.ui.employeeID.setText(employeeID)
        self.ui.supplierID.setText(supplierID)
        self.ui.purchaseDate.setText(purchaseDate)
        self.ui.totalCost.setText(totalCost)

        importResult = self.ipd.search(importID)
        self.ui.table.setRowCount(0)
        if importResult:
            self.ui.table.setRowCount(len(importResult))

            for row, info in enumerate(importResult):
                infoList = [
                    info["productID"],
                    info["quantity"],
                    info["price"],
                    info["cost"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return