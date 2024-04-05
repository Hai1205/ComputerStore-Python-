import mysql.connector

class Model_InvoiceDetail:
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
    
    def checkExist(self, invoiceID):
        self.open()
        query = f"""SELECT invoiceID FROM invoicedetail WHERE invoiceID LIKE '{invoiceID}';"""

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

    def add(self, invoiceID, productID, warrantyID, quantity, price, cost):
        self.open()
        query = f"""INSERT INTO invoicedetail (invoiceID, productID, warrantyID, quantity, price, cost)
                    VALUES ('{invoiceID}', '{productID}', '{warrantyID}', {quantity}, {price}, {cost});"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def listOfCustomer(self, customerID):
        if customerID == "admin":
            query = """CREATE TEMPORARY TABLE IF NOT EXISTS listOfCustomer AS 
                       SELECT * FROM invoicedetail"""
        else:
            query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS listOfCustomer AS
                        SELECT ivd.* FROM invoice iv
                        JOIN invoiceDetail ivd ON iv.invoiceID = ivd.invoiceID
                        WHERE iv.customerID LIKE '{customerID}';"""

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

    def search(self, invoiceID=None, productID=None, warrantyID=None, customerID=None, quantity=None, price=None, cost=None):
        self.open()
        self.listOfCustomer(customerID)

        condition = ""
        if invoiceID:
            condition += f"invoiceID LIKE '%{invoiceID}%'"
        else:
            if productID:
                if condition:
                    condition += f" and productID LIKE '%{productID}%'"
                else: 
                    condition += f"productID LIKE '%{productID}%'"
            if warrantyID:
                if condition:
                    condition += f" and warrantyID LIKE '%{warrantyID}%'"
                else:
                    condition += f"warrantyID LIKE '%{warrantyID}%'"
            if quantity:
                if condition:
                    condition += f" and quantity LIKE '%{quantity}%'"
                else:
                    condition += f"quantity LIKE '%{quantity}%'"
            if price:
                if condition:
                    condition += f" and price LIKE '%{price}%'"
                else:
                    condition += f"price LIKE '%{price}%'"
            if cost:
                if condition:
                    condition += f" and cost LIKE '%{cost}%'"
                else:
                    condition += f"cost LIKE '%{cost}%'"
        
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

    def delete(self, warrantyID):
        self.open()
        query = f"DELETE FROM invoicedetail WHERE warrantyID = '{warrantyID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()