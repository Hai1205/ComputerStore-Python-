import mysql.connector

class Model_Warranty:
    def __init__(self):
        self.User='root'
        self.Password=''
        self.Host='localhost'
        self.Database='computerstore'
        self.con = None
        self.cursor = None

    def open(self):
        self.con = mysql.connector.connect(
                user=self.User,
                password=self.Password,
                host=self.Host,
                database=self.Database
        )

        self.cursor = self.con.cursor(dictionary=True)
    
    def checkExist(self, warrantyID):
        self.open()
        query = f"""SELECT warrantyID FROM warranty WHERE warrantyID LIKE '{warrantyID}';"""

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def add(self, warrantyID, productID, invoiceID, customerID, purchaseDate, warrantyTime, EXP):
        self.open()
        query = f"""INSERT INTO warranty (warrantyID, productID, invoiceID, customerID, purchaseDate, warrantyTime, EXP)
                    VALUES ('{warrantyID}', '{productID}', '{invoiceID}', '{customerID}', '{purchaseDate}', {warrantyTime}, '{EXP}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, warrantyID, purchaseDate, warrantyTime):
        self.open()
        query = f"""UPDATE warranty 
                    SET purchaseDate = '{purchaseDate}', warrantyTime = {warrantyTime}, EXP = DATE_ADD(purchaseDate, INTERVAL {warrantyTime} MONTH)
                    WHERE warrantyID = '{warrantyID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, warrantyID):
        self.open()
        query = f"DELETE FROM warranty WHERE warrantyID = '{warrantyID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def listOfCustomer(self, customerID):
        where = ""
        if customerID != "admin":
            where = f"WHERE customerID LIKE '{customerID}'"

        query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS listOfCustomer AS
                    SELECT * FROM warranty
                    {where};"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        
    def dropListOfCustomer(self):
        query = f"""DROP TEMPORARY TABLE IF EXISTS listOfCustomer;"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)

    def search(self, warrantyID=None, productID=None, invoiceID=None, customerID=None, purchaseDate=None, warrantyTime=None, EXP=None):
        self.open()
        self.listOfCustomer(customerID)

        condition = ""
        if warrantyID:
            condition += f"warrantyID LIKE '%{warrantyID}%'"
        else:
            if productID:
                if condition:
                    condition += f" and productID LIKE '%{productID}%'"
                else: 
                    condition += f"productID LIKE '%{productID}%'"
            if invoiceID:
                if condition:
                    condition += f" and invoiceID LIKE '%{invoiceID}%'"
                else:
                    condition += f"invoiceID LIKE '%{invoiceID}%'"
            if purchaseDate:
                if condition:
                    condition += f" and purchaseDate <= '{purchaseDate}'"
                else:
                    condition += f"purchaseDate <= '{purchaseDate}'"
            if warrantyTime:
                if condition:
                    condition += f" and warrantyTime LIKE '%{warrantyTime}%'"
                else:
                    condition += f"warrantyTime LIKE '%{warrantyTime}%'"
            if EXP:
                if condition:
                    condition += f" and EXP <= '{EXP}'"
                else:
                    condition += f"EXP <= '{EXP}'"
        
        if condition:
            query = f"SELECT * FROM listOfCustomer WHERE {condition};"
        else:
            query = f"SELECT * FROM listOfCustomer;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.dropListOfCustomer()
            self.con.close()
    
    def expiryList(self, warrantyID=None, productID=None, invoiceID=None, customerID=None, purchaseDate=None, warrantyTime=None, EXP=None):
        self.open()
        self.listOfCustomer(customerID)

        condition = ""
        if warrantyID:
            condition += f"warrantyID LIKE '%{warrantyID}%'"
        else:
            if productID:
                if condition:
                    condition += f" and productID LIKE '%{productID}%'"
                else: 
                    condition += f"productID LIKE '%{productID}%'"
            if invoiceID:
                if condition:
                    condition += f" and invoiceID LIKE '%{invoiceID}%'"
                else:
                    condition += f"invoiceID LIKE '%{invoiceID}%'"
            if purchaseDate:
                if condition:
                    condition += f" and purchaseDate LIKE '%{purchaseDate}%'"
                else:
                    condition += f"purchaseDate LIKE '%{purchaseDate}%'"
            if warrantyTime:
                if condition:
                    condition += f" and warrantyTime LIKE '%{warrantyTime}%'"
                else:
                    condition += f"warrantyTime LIKE '%{warrantyTime}%'"
            if EXP:
                if condition:
                    condition += f" and EXP LIKE '%{EXP}%'"
                else:
                    condition += f"EXP LIKE '%{EXP}%'"
        
        if condition:
            query = f"SELECT * FROM listOfCustomer WHERE {condition} and EXP > CURRENT_DATE();;"
        else:
            query = f"SELECT * FROM listOfCustomer WHERE EXP > CURRENT_DATE();;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.dropListOfCustomer()
            self.con.close()

