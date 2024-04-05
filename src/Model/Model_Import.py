import mysql.connector

class Model_Import:
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
    
    def checkExist(self, importID):
        self.open()
        query = f"""SELECT importID FROM import WHERE importID LIKE '{importID}';"""

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
    
    def add(self, importID, employeeID, supplierID, date, totalCost):
        self.open()
        query = f"""INSERT INTO import (importID, employeeID, supplierID, date, totalCost)
                    VALUES ('{importID}', '{employeeID}', '{supplierID}', '{date}', {totalCost});"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, importID, date, totalCost):
        self.open()
        query = f"""UPDATE import SET date = '{date}', totalCost = '{totalCost}' WHERE importID = '{importID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, importID):
        self.open()
        query = f"DELETE FROM import WHERE importID = '{importID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, importID=None, employeeID=None, supplierID=None, date=None, totalCost=None):
        self.open()

        condition = ""
        if importID:
            condition += f"importID LIKE '%{importID}%'"
        else:
            if employeeID:
                if condition:
                    condition += f" and employeeID LIKE '%{employeeID}%'"
                else: 
                    condition += f"employeeID LIKE '%{employeeID}%'"
            if supplierID:
                if condition:
                    condition += f" and supplierID LIKE '%{supplierID}%'"
                else:
                    condition += f"supplierID LIKE '%{supplierID}%'"
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
            query = f"SELECT * FROM import WHERE {condition};"
        else:
            query = f"SELECT * FROM import;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()
