from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate

from View.EmployeeAdmin import Ui_EmployeeAdmin

from Model.Model_Employee import Model_Employee

from Controller.Controller import Controller

class EmployeeAdmin(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_EmployeeAdmin()
        self.ui.setupUi(self)

        self.employeeID = None
        self.selectRow = -1

        self.ep = Model_Employee()

        self.button()
    
    def button(self):
        self.ui.statistic.clicked.connect(self.statistic)
        self.ui.signOut.clicked.connect(self.signOut)

        self.ui.product.clicked.connect(self.product)
        self.ui.import_2.clicked.connect(self.import_2)
        self.ui.customer.clicked.connect(self.customer)
        self.ui.supplier.clicked.connect(self.supplier)
        self.ui.warranty.clicked.connect(self.warranty)
        self.ui.invoice.clicked.connect(self.invoice)
        self.ui.account.clicked.connect(self.account)

        self.ui.select.clicked.connect(self.select)
        self.ui.add.clicked.connect(self.add)
        self.ui.update.clicked.connect(self.update)
        self.ui.search.clicked.connect(self.search)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.delete_2.clicked.connect(self.delete_2)


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

    def account(self):
        self.general.showAccountAdmin()
        self.general.page(2)

    def select(self):
        self.setEnabled(False)
        self.selectRow = self.ui.table.currentRow()
        if self.selectRow != -1:
            employeeID = self.ui.table.item(self.selectRow, 0).text().strip()
            firstname = self.ui.table.item(self.selectRow, 1).text().strip()
            lastname = self.ui.table.item(self.selectRow, 2).text().strip()
            DOB = self.ui.table.item(self.selectRow, 3).text().strip()
            position = self.ui.table.item(self.selectRow, 4).text().strip()
            salary = self.ui.table.item(self.selectRow, 5).text().strip()

            self.ui.employeeID.setText(employeeID)
            self.ui.firstname.setText(firstname)
            self.ui.lastname.setText(lastname)
            self.ui.DOB.setDate(QDate.fromString(DOB, "yyyy-MM-dd"))
            self.ui.position.setCurrentText(position)
            self.ui.salary.setText(salary)

    def add(self):
        employee = self.getEmployee()
        employeeID = ""
        if employeeID == "":
            while True:
                employeeID = Controller.createEmployeeID()
                if not self.ep.checkExist(employeeID):
                    break
        firstname = employee["firstname"]
        lastname = employee["lastname"]
        DOB = Controller.strToDate(employee["DOB"])
        position = employee["position"]
        salary = employee["salary"]

        if position == "All":
            QMessageBox.information(self, "Add Error", "Please choose a different position than All.")
            return 

        self.ep.add(employeeID, firstname, lastname, DOB, position, salary)

        QMessageBox.information(self, "Add Confirmation", "Employee has been added successfully.")
        self.clear()

    def update(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Update Error", "Please select the employee.")
            return
        
        employee = self.getEmployee()
        employeeID = employee["employeeID"]
        firstname = employee["firstname"]
        lastname = employee["lastname"]
        DOB = Controller.strToDate(employee["DOB"])
        position = employee["position"]
        salary = employee["salary"]

        self.ep.update(employeeID, firstname, lastname, DOB, position, salary)
        self.search()

    def search(self):
        employee = self.getEmployee()
        position=employee["position"]
        if position == "All":
            position = None
        employeeResult = self.ep.search(employeeID=employee["employeeID"],
                                    firstname=employee["firstname"],
                                    lastname=employee["lastname"],
                                    DOB=employee["DOB"],
                                    position=position,
                                    salary=employee["salary"],
        )
        self.showData(employeeResult)
    
    def showData(self, employeeResult):
        self.ui.table.setRowCount(0)
        if employeeResult:
            self.ui.table.setRowCount(len(employeeResult))

            for row, info in enumerate(employeeResult):
                infoList = [
                    info["employeeID"],
                    info["firstname"],
                    info["lastname"],
                    info["DOB"],
                    info["position"],
                    info["salary"],
                ]

                for column, item in enumerate(infoList):
                    cellItem = QTableWidgetItem(str(item))
                    self.ui.table.setItem(row, column, cellItem)
        
        else:
            return
        
    def getEmployee(self):
        employeeID = self.ui.employeeID.text().strip()
        firstname = self.ui.firstname.text().strip()
        lastname = self.ui.lastname.text().strip()
        DOB = self.ui.DOB.text().strip()
        position = self.ui.position.currentText().strip()
        salary = self.ui.salary.text().strip()

        employee = {
            "employeeID": employeeID,
            "firstname": firstname,
            "lastname": lastname,
            "DOB": DOB,
            "position": position,
            "salary": salary
        }

        return employee

    def setEnabled(self, bool):
        self.ui.employeeID.setEnabled(bool)

    def clear(self):
        self.selectRow = -1
        self.ui.employeeID.clear()
        self.ui.firstname.clear()
        self.ui.lastname.clear()
        self.ui.DOB.setDate(QDate(2000, 1, 1))
        self.ui.position.setCurrentIndex(0)
        self.ui.salary.clear()
        self.search()
        self.setEnabled(True)

    def delete_2(self):
        if self.selectRow == -1:
            QMessageBox.information(self, "Delete Error", "Please select the employee.")
            return
        confirmRefund = QMessageBox.question(self, "Warning", "Are you sure want to delete?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmRefund == QMessageBox.StandardButton.No:
            return
        
        employee = self.getEmployee()
        employeeID = employee["employeeID"]
        self.ep.delete(employeeID)
        QMessageBox.information(self, "Delete Confirmation", "Employee has been deleted successfully.")
        self.clear()
