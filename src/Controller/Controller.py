import random
import re
from datetime import datetime

class Controller:
    @staticmethod
    def createCustomerID():
        return "CTM" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def createEmployeeID():
        return "EP" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def createImportID():
        return "IP" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def createInvoiceID():
        return "IV" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def createProductID():
        return "PD" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def createSupplierID():
        return "SP" + str(random.randint(10**9, (10**10)-1))
    
    @staticmethod
    def createWarrantyID():
        return "WRT" + str(random.randint(10**9, (10**10)-1))

    @staticmethod
    def compare_dates(date1, date2):
        return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

    @staticmethod
    def strToDate(date):
        return datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

    @staticmethod
    def checkPhone(phone):
        pattern = r'^\+?[0-9]{9,10}$'
    
        if re.match(pattern, phone):
            return True
        else:
            return False




