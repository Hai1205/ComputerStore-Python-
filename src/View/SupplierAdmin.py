# Form implementation generated from reading ui file 'SupplierAdmin.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SupplierAdmin(object):
    def setupUi(self, SupplierAdmin):
        SupplierAdmin.setObjectName("SupplierAdmin")
        SupplierAdmin.resize(1163, 768)
        font = QtGui.QFont()
        font.setPointSize(13)
        SupplierAdmin.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=SupplierAdmin)
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
        self.table.setColumnCount(4)
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
        self.table.horizontalHeader().setDefaultSectionSize(250)
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
        self.supplierName = QtWidgets.QLineEdit(parent=self.frame_6)
        self.supplierName.setObjectName("supplierName")
        self.gridLayout.addWidget(self.supplierName, 1, 1, 1, 1)
        self.supplierID = QtWidgets.QLineEdit(parent=self.frame_6)
        self.supplierID.setObjectName("supplierID")
        self.gridLayout.addWidget(self.supplierID, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(520, 40, 421, 251))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(parent=self.frame_7)
        self.email.setObjectName("email")
        self.gridLayout_2.addWidget(self.email, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.address = QtWidgets.QLineEdit(parent=self.frame_7)
        self.address.setObjectName("address")
        self.gridLayout_2.addWidget(self.address, 1, 1, 1, 1)
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
        self.add = QtWidgets.QPushButton(parent=self.frame_4)
        self.add.setObjectName("add")
        self.horizontalLayout_2.addWidget(self.add)
        self.update = QtWidgets.QPushButton(parent=self.frame_4)
        self.update.setObjectName("update")
        self.horizontalLayout_2.addWidget(self.update)
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
        SupplierAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SupplierAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        SupplierAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SupplierAdmin)
        self.statusbar.setObjectName("statusbar")
        SupplierAdmin.setStatusBar(self.statusbar)

        self.retranslateUi(SupplierAdmin)
        QtCore.QMetaObject.connectSlotsByName(SupplierAdmin)

    def retranslateUi(self, SupplierAdmin):
        _translate = QtCore.QCoreApplication.translate
        SupplierAdmin.setWindowTitle(_translate("SupplierAdmin", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("SupplierAdmin", "SupplierID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("SupplierAdmin", "Supplier name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("SupplierAdmin", "Email"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("SupplierAdmin", "Address"))
        self.label.setText(_translate("SupplierAdmin", "Supplier"))
        self.label_3.setText(_translate("SupplierAdmin", "Supplier name"))
        self.label_2.setText(_translate("SupplierAdmin", "SupplierID"))
        self.label_4.setText(_translate("SupplierAdmin", "Email"))
        self.label_5.setText(_translate("SupplierAdmin", "Address"))
        self.management.setText(_translate("SupplierAdmin", "Management"))
        self.statistic.setText(_translate("SupplierAdmin", "Stastistics"))
        self.signOut.setText(_translate("SupplierAdmin", "Sign out"))
        self.select.setText(_translate("SupplierAdmin", "Select"))
        self.add.setText(_translate("SupplierAdmin", "Add"))
        self.update.setText(_translate("SupplierAdmin", "Update"))
        self.search.setText(_translate("SupplierAdmin", "Search"))
        self.clear.setText(_translate("SupplierAdmin", "Clear"))
        self.delete_2.setText(_translate("SupplierAdmin", "Delete"))
        self.product.setText(_translate("SupplierAdmin", "Product"))
        self.import_2.setText(_translate("SupplierAdmin", "Import"))
        self.customer.setText(_translate("SupplierAdmin", "Customer"))
        self.supplier.setText(_translate("SupplierAdmin", "Supplier"))
        self.warranty.setText(_translate("SupplierAdmin", "Warranty"))
        self.invoice.setText(_translate("SupplierAdmin", "Invoice"))
        self.employee.setText(_translate("SupplierAdmin", "Employee"))
        self.account.setText(_translate("SupplierAdmin", "Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SupplierAdmin = QtWidgets.QMainWindow()
    ui = Ui_SupplierAdmin()
    ui.setupUi(SupplierAdmin)
    SupplierAdmin.show()
    sys.exit(app.exec())
