from PyQt6.QtWidgets import QMainWindow, QMessageBox

from View.ProductDetail import Ui_ProductDetail

from Model.Model_ProductDetail import Model_ProductDetail

class ProductDetail(QMainWindow):
    def __init__(self, general):
        super().__init__()
        self.general = general
        self.ui = Ui_ProductDetail()
        self.ui.setupUi(self)

        self.pdd = Model_ProductDetail()
        
        self.customerID = None
        self.product = None

        self.button()
    
    def setCustomerID(self, customerID):
        self.customerID = customerID
    
    def setProduct(self, product):
        self.product = product
    
    def button(self):
        self.ui.back.clicked.connect(self.back)
    
    def back(self):
        if self.customerID == "admin":
            self.general.page(7)
        else:
            self.general.page(11)
    
    def showData(self):
        self.ui.productID.setText(self.product["productID"])
        self.ui.supplierName.setText(self.product["supplierName"])
        self.ui.productName.setText(self.product["productName"])
        self.ui.type.setText(self.product["type"])
        self.ui.warrantyTime.setText(self.product["warrantyTime"])
        self.ui.price.setText(self.product["price"])

        detail = self.pdd.search(self.product["productID"])
        data = ""
        type = self.product["type"]
        if type == "Laptop":
            data = f""" 
            Type: {detail[0]["type"]}

            Manufacturing date: {detail[0]["MFG"]}

            Random access memory: {detail[0]["RAM"]}
            
            Read-only memory: {detail[0]["ROM"]}
                        
            Central Processing Unit: {detail[0]["CPU"]}
                        
            Video Graphics Adaptor: {detail[0]["VGA"]}
                        
            Keyboard: {detail[0]["keyboard"]}
                        
            Screen: {detail[0]["screen"]}
                        
            Operating System: {detail[0]["OS"]}
                        
            Size: {detail[0]["size"]}
                        
            Pin: {detail[0]["pin"]}"""
        elif type == "RAM":
            data = f""" 
            Type: {detail[0]["type"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            Capacity: {detail[0]["capacity"]}
            
            Serial Presence Detect speed: {detail[0]["SPDspeed"]}
            
            CAS Latency: {detail[0]["CL"]}
            
            Size: {detail[0]["size"]}"""
        elif type == "ROM":
            data = f""" 
            Type: {detail[0]["type"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            Capacity: {detail[0]["capacity"]}
            
            Write speed: {detail[0]["writeSpeed"]}
            
            Read speed: {detail[0]["readSpeed"]}"""
        elif type == "CPU":
            data = f""" 
            Series: {detail[0]["series"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            Cores: {detail[0]["cores"]}
            
            Threads: {detail[0]["threads"]}"""
        elif type == "VGA":
            data = f""" 
            Cores: {detail[0]["cores"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            GPU clock: {detail[0]["GPUclock"]}
            
            Size: {detail[0]["size"]}"""
        elif type == "keyboard":
            data = f""" 
            Layout: {detail[0]["layout"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            Led: {detail[0]["led"]}
            
            Size: {detail[0]["size"]}
            
            Keycap: {detail[0]["keycap"]}
            
            Switch date: {detail[0]["switch"]}
            
            Pin: {detail[0]["pin"]}
            
            Hotswap: {detail[0]["hotswap"]}"""
        elif type == "screen":
            data = f""" 
            Scan: {detail[0]["scan"]}
            
            Manufacturing date: {detail[0]["MFG"]}
            
            Size: {detail[0]["size"]}
            
            Panel: {detail[0]["panel"]}
            
            Resolution: {detail[0]["resolution"]}"""
        
        self.ui.detail.append(data)