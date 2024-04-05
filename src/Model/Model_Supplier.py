import mysql.connector

class Model_Supplier:
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
    
    def checkExist(self, supplierID):
        self.open()
        query = f"""SELECT supplierID FROM supplier WHERE supplierID LIKE '{supplierID}';"""

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
    
    def add(self, supplierID, supplierName):
        self.open()
        query = f"""INSERT INTO supplier (supplierID, supplierName)
                    VALUES ('{supplierID}', '{supplierName}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, supplierID, supplierName):
        self.open()
        query = f"""UPDATE supplier 
                    SET supplierName = '{supplierName}' WHERE supplierID = '{supplierID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, supplierID):
        self.open()
        query = f"DELETE FROM supplier WHERE supplierID = '{supplierID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, supplierID=None, supplierName=None):
        self.open()

        condition = ""
        if supplierID:
            condition += f"supplierID LIKE '%{supplierID}%'"
        elif supplierName:
            if condition:
                condition += f" and supplierName LIKE '%{supplierName}%'"
            else: 
                condition += f"supplierName LIKE '%{supplierName}%'"
            
        if condition:
            query = f"SELECT * FROM supplier WHERE {condition};"
        else:
            query = f"SELECT * FROM supplier;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()
