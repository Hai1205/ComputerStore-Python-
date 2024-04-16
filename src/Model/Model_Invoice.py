import mysql.connector

class Model_Invoice:
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
        query = f"""SELECT invoiceID FROM invoice WHERE invoiceID LIKE '{invoiceID}';"""

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
    
    def getDate(self, invoiceID):
        self.open()
        query = f"""SELECT date FROM invoice WHERE invoiceID LIKE '{invoiceID}';"""

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def add(self, invoiceID, employeeID, customerID, date, totalCost):
        self.open()
        query = f"""INSERT INTO invoice (invoiceID, employeeID, customerID, date, totalCost)
                    VALUES ('{invoiceID}', '{employeeID}', '{customerID}', '{date}', {totalCost});"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, invoiceID, date, totalCost):
        self.open()
        query = f"""UPDATE invoice SET date = '{date}', totalCost = '{totalCost}' WHERE invoiceID = '{invoiceID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def decreaseTotalCost(self, invoiceID, value):
        self.open()
        query = f"""UPDATE invoice 
                    SET totalcost = totalcost - {value}
                    WHERE invoiceID = '{invoiceID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, invoiceID):
        self.open()
        query = f"DELETE FROM invoice WHERE invoiceID = '{invoiceID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, invoiceID=None, employeeID=None, customerID=None, date=None, totalCost=None):
        self.open()

        condition = ""
        if invoiceID:
            condition += f"invoiceID LIKE '%{invoiceID}%'"
        else:
            if employeeID:
                if condition:
                    condition += f" and employeeID LIKE '%{employeeID}%'"
                else: 
                    condition += f"employeeID LIKE '%{employeeID}%'"
            if customerID:
                if condition:
                    condition += f" and customerID LIKE '%{customerID}%'"
                else:
                    condition += f"customerID LIKE '%{customerID}%'"
            if date:
                if condition:
                    condition += f" and date <= '{date}'"
                else:
                    condition += f"date <= '{date}'"
            if totalCost:
                if condition:
                    condition += f" and totalCost LIKE '%{totalCost}%'"
                else:
                    condition += f"totalCost LIKE '%{totalCost}%'"
        
        if condition:
            query = f"SELECT * FROM invoice WHERE {condition};"
        else:
            query = f"SELECT * FROM invoice;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()

    def getYearsAndTotal(self):
        self.open()
        
        query = """SELECT YEAR(date) as year, SUM(totalCost) as total
                    FROM invoice
                    GROUP BY YEAR(date);"""

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()