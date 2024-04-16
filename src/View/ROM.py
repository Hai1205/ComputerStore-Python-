# Form implementation generated from reading ui file 'ROM.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ROM(object):
    def setupUi(self, ROM):
        ROM.setObjectName("ROM")
        ROM.resize(1163, 768)
        font = QtGui.QFont()
        font.setPointSize(13)
        ROM.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=ROM)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(160, 89, 1001, 621))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.productName = QtWidgets.QLabel(parent=self.frame_2)
        self.productName.setGeometry(QtCore.QRect(0, 0, 941, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.productName.setFont(font)
        self.productName.setText("")
        self.productName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.productName.setObjectName("productName")
        self.frame = QtWidgets.QFrame(parent=self.frame_2)
        self.frame.setGeometry(QtCore.QRect(0, 70, 591, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.capacity = QtWidgets.QLineEdit(parent=self.frame)
        self.capacity.setObjectName("capacity")
        self.gridLayout.addWidget(self.capacity, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.readSpeed = QtWidgets.QLineEdit(parent=self.frame)
        self.readSpeed.setObjectName("readSpeed")
        self.gridLayout.addWidget(self.readSpeed, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.writeSpeed = QtWidgets.QLineEdit(parent=self.frame)
        self.writeSpeed.setObjectName("writeSpeed")
        self.gridLayout.addWidget(self.writeSpeed, 4, 1, 1, 1)
        self.type = QtWidgets.QLineEdit(parent=self.frame)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 3, 1, 1, 1)
        self.MFG = QtWidgets.QLineEdit(parent=self.frame)
        self.MFG.setObjectName("MFG")
        self.gridLayout.addWidget(self.MFG, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(240, 530, 481, 81))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.update = QtWidgets.QPushButton(parent=self.frame_6)
        self.update.setObjectName("update")
        self.gridLayout_3.addWidget(self.update, 0, 1, 1, 1)
        self.back = QtWidgets.QPushButton(parent=self.frame_6)
        self.back.setObjectName("back")
        self.gridLayout_3.addWidget(self.back, 0, 3, 1, 1)
        self.add = QtWidgets.QPushButton(parent=self.frame_6)
        self.add.setObjectName("add")
        self.gridLayout_3.addWidget(self.add, 0, 0, 1, 1)
        self.clear = QtWidgets.QPushButton(parent=self.frame_6)
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 0, 2, 1, 1)
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
        ROM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ROM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        ROM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ROM)
        self.statusbar.setObjectName("statusbar")
        ROM.setStatusBar(self.statusbar)

        self.retranslateUi(ROM)
        QtCore.QMetaObject.connectSlotsByName(ROM)

    def retranslateUi(self, ROM):
        _translate = QtCore.QCoreApplication.translate
        ROM.setWindowTitle(_translate("ROM", "MainWindow"))
        self.label_4.setText(_translate("ROM", "Capacity:"))
        self.label_2.setText(_translate("ROM", "Manufacturing date:"))
        self.label_6.setText(_translate("ROM", "Read speed:"))
        self.label_3.setText(_translate("ROM", "Write speed:"))
        self.label_5.setText(_translate("ROM", "Type:"))
        self.update.setText(_translate("ROM", "Update"))
        self.back.setText(_translate("ROM", "Back"))
        self.add.setText(_translate("ROM", "Add"))
        self.clear.setText(_translate("ROM", "Clear"))
        self.management.setText(_translate("ROM", "Management"))
        self.statistic.setText(_translate("ROM", "Stastistics"))
        self.signOut.setText(_translate("ROM", "Sign out"))
        self.product.setText(_translate("ROM", "Product"))
        self.import_2.setText(_translate("ROM", "Import"))
        self.customer.setText(_translate("ROM", "Customer"))
        self.supplier.setText(_translate("ROM", "Supplier"))
        self.warranty.setText(_translate("ROM", "Warranty"))
        self.invoice.setText(_translate("ROM", "Invoice"))
        self.employee.setText(_translate("ROM", "Employee"))
        self.account.setText(_translate("ROM", "Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ROM = QtWidgets.QMainWindow()
    ui = Ui_ROM()
    ui.setupUi(ROM)
    ROM.show()
    sys.exit(app.exec())
