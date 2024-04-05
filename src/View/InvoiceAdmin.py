# Form implementation generated from reading ui file 'InvoiceAdmin.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InvoiceAdmin(object):
    def setupUi(self, InvoiceAdmin):
        InvoiceAdmin.setObjectName("InvoiceAdmin")
        InvoiceAdmin.resize(1163, 768)
        font = QtGui.QFont()
        font.setPointSize(13)
        InvoiceAdmin.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=InvoiceAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 460, 1151, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.table = QtWidgets.QTableWidget(parent=self.frame)
        self.table.setGeometry(QtCore.QRect(70, 20, 1021, 231))
        self.table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.table.setShowGrid(False)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(35)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(160, 89, 1001, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(410, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(-1, 39, 411, 251))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.invoiceID = QtWidgets.QLineEdit(parent=self.frame_6)
        self.invoiceID.setObjectName("invoiceID")
        self.gridLayout.addWidget(self.invoiceID, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.employeeID = QtWidgets.QLineEdit(parent=self.frame_6)
        self.employeeID.setObjectName("employeeID")
        self.gridLayout.addWidget(self.employeeID, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.customerID = QtWidgets.QLineEdit(parent=self.frame_6)
        self.customerID.setObjectName("customerID")
        self.gridLayout.addWidget(self.customerID, 2, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(510, 39, 431, 251))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.totalCost = QtWidgets.QLineEdit(parent=self.frame_7)
        self.totalCost.setObjectName("totalCost")
        self.gridLayout_2.addWidget(self.totalCost, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.date = QtWidgets.QDateEdit(parent=self.frame_7)
        self.date.setObjectName("date")
        self.gridLayout_2.addWidget(self.date, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 515, 56))
        self.frame_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.management = QtWidgets.QPushButton(parent=self.frame_3)
        self.management.setObjectName("management")
        self.horizontalLayout.addWidget(self.management)
        self.statistic = QtWidgets.QPushButton(parent=self.frame_3)
        self.statistic.setObjectName("statistic")
        self.horizontalLayout.addWidget(self.statistic)
        self.signOut = QtWidgets.QPushButton(parent=self.frame_3)
        self.signOut.setObjectName("signOut")
        self.horizontalLayout.addWidget(self.signOut)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(149, 379, 951, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select = QtWidgets.QPushButton(parent=self.frame_4)
        self.select.setObjectName("select")
        self.horizontalLayout_2.addWidget(self.select)
        self.detail = QtWidgets.QPushButton(parent=self.frame_4)
        self.detail.setObjectName("detail")
        self.horizontalLayout_2.addWidget(self.detail)
        self.search = QtWidgets.QPushButton(parent=self.frame_4)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.clear = QtWidgets.QPushButton(parent=self.frame_4)
        self.clear.setObjectName("clear")
        self.horizontalLayout_2.addWidget(self.clear)
        self.delete_2 = QtWidgets.QPushButton(parent=self.frame_4)
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout_2.addWidget(self.delete_2)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 90, 138, 350))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.product = QtWidgets.QPushButton(parent=self.frame_5)
        self.product.setObjectName("product")
        self.verticalLayout.addWidget(self.product)
        self.import_2 = QtWidgets.QPushButton(parent=self.frame_5)
        self.import_2.setObjectName("import_2")
        self.verticalLayout.addWidget(self.import_2)
        self.customer = QtWidgets.QPushButton(parent=self.frame_5)
        self.customer.setObjectName("customer")
        self.verticalLayout.addWidget(self.customer)
        self.supplier = QtWidgets.QPushButton(parent=self.frame_5)
        self.supplier.setObjectName("supplier")
        self.verticalLayout.addWidget(self.supplier)
        self.warranty = QtWidgets.QPushButton(parent=self.frame_5)
        self.warranty.setObjectName("warranty")
        self.verticalLayout.addWidget(self.warranty)
        self.invoice = QtWidgets.QPushButton(parent=self.frame_5)
        self.invoice.setObjectName("invoice")
        self.verticalLayout.addWidget(self.invoice)
        self.employee = QtWidgets.QPushButton(parent=self.frame_5)
        self.employee.setObjectName("employee")
        self.verticalLayout.addWidget(self.employee)
        self.account = QtWidgets.QPushButton(parent=self.frame_5)
        self.account.setObjectName("account")
        self.verticalLayout.addWidget(self.account)
        InvoiceAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=InvoiceAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        InvoiceAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=InvoiceAdmin)
        self.statusbar.setObjectName("statusbar")
        InvoiceAdmin.setStatusBar(self.statusbar)

        self.retranslateUi(InvoiceAdmin)
        QtCore.QMetaObject.connectSlotsByName(InvoiceAdmin)

    def retranslateUi(self, InvoiceAdmin):
        _translate = QtCore.QCoreApplication.translate
        InvoiceAdmin.setWindowTitle(_translate("InvoiceAdmin", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("InvoiceAdmin", "InvoiceID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("InvoiceAdmin", "EmployeeID"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("InvoiceAdmin", "CustomerID"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("InvoiceAdmin", "Date"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("InvoiceAdmin", "Total cost"))
        self.label.setText(_translate("InvoiceAdmin", "Invoice"))
        self.label_3.setText(_translate("InvoiceAdmin", "EmployeeID"))
        self.label_2.setText(_translate("InvoiceAdmin", "InvoiceID"))
        self.label_6.setText(_translate("InvoiceAdmin", "CustomerID"))
        self.label_5.setText(_translate("InvoiceAdmin", "Date"))
        self.label_4.setText(_translate("InvoiceAdmin", "Total cost"))
        self.management.setText(_translate("InvoiceAdmin", "Management"))
        self.statistic.setText(_translate("InvoiceAdmin", "Stastistics"))
        self.signOut.setText(_translate("InvoiceAdmin", "Sign out"))
        self.select.setText(_translate("InvoiceAdmin", "Select"))
        self.detail.setText(_translate("InvoiceAdmin", "Detail"))
        self.search.setText(_translate("InvoiceAdmin", "Search"))
        self.clear.setText(_translate("InvoiceAdmin", "Clear"))
        self.delete_2.setText(_translate("InvoiceAdmin", "Delete"))
        self.product.setText(_translate("InvoiceAdmin", "Product"))
        self.import_2.setText(_translate("InvoiceAdmin", "Import"))
        self.customer.setText(_translate("InvoiceAdmin", "Customer"))
        self.supplier.setText(_translate("InvoiceAdmin", "Supplier"))
        self.warranty.setText(_translate("InvoiceAdmin", "Warranty"))
        self.invoice.setText(_translate("InvoiceAdmin", "Invoice"))
        self.employee.setText(_translate("InvoiceAdmin", "Employee"))
        self.account.setText(_translate("InvoiceAdmin", "Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InvoiceAdmin = QtWidgets.QMainWindow()
    ui = Ui_InvoiceAdmin()
    ui.setupUi(InvoiceAdmin)
    InvoiceAdmin.show()
    sys.exit(app.exec())
