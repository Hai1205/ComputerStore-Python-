import mysql.connector

class Model_ImportDetail:
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

    def add(self, importID, productID, quantity, price, cost):
        self.open()
        query = f"""INSERT INTO importdetail (importID, productID, quantity, price, cost)
                    VALUES ('{importID}', '{productID}', {quantity}, {price}, {cost});"""

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
        query = f"DELETE FROM importdetail WHERE importID = '{importID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def search(self, importID=None, productID=None):
        self.open()

        condition = ""
        if importID:
            condition += f"importID LIKE '%{importID}%'"
        else:
            if productID:
                if condition:
                    condition += f" and productID LIKE '%{productID}%'"
                else: 
                    condition += f"productID LIKE '%{productID}%'"
        
        if condition:
            query = f"SELECT * FROM importdetail WHERE {condition};"
        else:
            query = f"SELECT * FROM importdetail;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()