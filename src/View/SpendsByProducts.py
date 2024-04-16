# Form implementation generated from reading ui file 'SpendsByProducts.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpendsByProducts(object):
    def setupUi(self, SpendsByProducts):
        SpendsByProducts.setObjectName("SpendsByProducts")
        SpendsByProducts.resize(1163, 768)
        font = QtGui.QFont()
        font.setPointSize(13)
        SpendsByProducts.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=SpendsByProducts)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(250, 40, 911, 611))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.graph = QtWidgets.QLabel(parent=self.frame_2)
        self.graph.setGeometry(QtCore.QRect(14, 105, 881, 421))
        self.graph.setText("")
        self.graph.setObjectName("graph")
        self.frame = QtWidgets.QFrame(parent=self.frame_2)
        self.frame.setGeometry(QtCore.QRect(9, 550, 381, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.totalCost = QtWidgets.QLabel(parent=self.frame)
        self.totalCost.setText("")
        self.totalCost.setObjectName("totalCost")
        self.horizontalLayout_2.addWidget(self.totalCost)
        self.table = QtWidgets.QTableWidget(parent=self.frame_2)
        self.table.setGeometry(QtCore.QRect(30, 120, 861, 391))
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
        self.table.horizontalHeader().setDefaultSectionSize(214)
        self.message = QtWidgets.QLabel(parent=self.frame_2)
        self.message.setGeometry(QtCore.QRect(30, 70, 861, 31))
        self.message.setObjectName("message")
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
        self.statistics = QtWidgets.QPushButton(parent=self.frame_3)
        self.statistics.setObjectName("statistics")
        self.horizontalLayout.addWidget(self.statistics)
        self.signOut = QtWidgets.QPushButton(parent=self.frame_3)
        self.signOut.setObjectName("signOut")
        self.horizontalLayout.addWidget(self.signOut)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 90, 221, 461))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.salesByYears = QtWidgets.QPushButton(parent=self.frame_5)
        self.salesByYears.setObjectName("salesByYears")
        self.verticalLayout.addWidget(self.salesByYears)
        self.salesByEmployees = QtWidgets.QPushButton(parent=self.frame_5)
        self.salesByEmployees.setObjectName("salesByEmployees")
        self.verticalLayout.addWidget(self.salesByEmployees)
        self.salesByProducts = QtWidgets.QPushButton(parent=self.frame_5)
        self.salesByProducts.setObjectName("salesByProducts")
        self.verticalLayout.addWidget(self.salesByProducts)
        self.spendsByYears = QtWidgets.QPushButton(parent=self.frame_5)
        self.spendsByYears.setObjectName("spendsByYears")
        self.verticalLayout.addWidget(self.spendsByYears)
        self.spendsBySuppliers = QtWidgets.QPushButton(parent=self.frame_5)
        self.spendsBySuppliers.setObjectName("spendsBySuppliers")
        self.verticalLayout.addWidget(self.spendsBySuppliers)
        self.spendsByProducts = QtWidgets.QPushButton(parent=self.frame_5)
        self.spendsByProducts.setObjectName("spendsByProducts")
        self.verticalLayout.addWidget(self.spendsByProducts)
        SpendsByProducts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SpendsByProducts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        SpendsByProducts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SpendsByProducts)
        self.statusbar.setObjectName("statusbar")
        SpendsByProducts.setStatusBar(self.statusbar)

        self.retranslateUi(SpendsByProducts)
        QtCore.QMetaObject.connectSlotsByName(SpendsByProducts)

    def retranslateUi(self, SpendsByProducts):
        _translate = QtCore.QCoreApplication.translate
        SpendsByProducts.setWindowTitle(_translate("SpendsByProducts", "MainWindow"))
        self.label.setText(_translate("SpendsByProducts", "Spends by products"))
        self.label_2.setText(_translate("SpendsByProducts", "Total cost:"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("SpendsByProducts", "ProductID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("SpendsByProducts", "Product name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("SpendsByProducts", "Cost"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("SpendsByProducts", "Quantity"))
        self.message.setText(_translate("SpendsByProducts", "Statistics are taken from the beginning of the year until the present time."))
        self.management.setText(_translate("SpendsByProducts", "Management"))
        self.statistics.setText(_translate("SpendsByProducts", "Stastistics"))
        self.signOut.setText(_translate("SpendsByProducts", "Sign out"))
        self.salesByYears.setText(_translate("SpendsByProducts", "Sales by years"))
        self.salesByEmployees.setText(_translate("SpendsByProducts", "Sales by employees"))
        self.salesByProducts.setText(_translate("SpendsByProducts", "Sales by products"))
        self.spendsByYears.setText(_translate("SpendsByProducts", "Spends by years"))
        self.spendsBySuppliers.setText(_translate("SpendsByProducts", "Spends by suppliers"))
        self.spendsByProducts.setText(_translate("SpendsByProducts", "Spends by products"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpendsByProducts = QtWidgets.QMainWindow()
    ui = Ui_SpendsByProducts()
    ui.setupUi(SpendsByProducts)
    SpendsByProducts.show()
    sys.exit(app.exec())
