import mysql.connector

class Model_Customer:
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
    
    def checkExist(self, customerID):
        self.open()
        query = f"""SELECT customerID FROM customer WHERE customerID LIKE '{customerID}';"""

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

    
    def add(self, customerID, firstname, lastname, address, phone):
        self.open()
        query = f"""INSERT INTO customer (customerID, firstname, lastname, address, phone)
                    VALUES ('{customerID}', '{firstname}', '{lastname}', '{address}', '{phone}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, customerID, firstname, lastname, address, phone):
        self.open()
        
        condition = ""
        if firstname:
            condition += f" firstname = '{firstname}'"
        if lastname:
            if condition:
                condition += f", lastname = '{lastname}'"
            else:
                condition += f"lastname = '{lastname}'"
        if address:
            if condition:
                condition += f", address = '{address}'"
            else:
                condition += f"address = '{address}'"
        if phone:
            if condition:
                condition += f", phone = '{phone}'"
            else:
                condition += f"phone = '{phone}'"
            
        
        query = f"""UPDATE customer SET {condition} 
                    WHERE customerID = '{customerID}';"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, customerID):
        self.open()
        query = f"DELETE FROM customer WHERE customerID = '{customerID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, customerID=None, firstname=None, lastname=None, address=None, phone=None):
        self.open()

        condition = ""
        if customerID:
            condition += f"customerID LIKE '%{customerID}%'"
        else:
            if firstname:
                if condition:
                    condition += f" and firstname LIKE '%{firstname}%'"
                else: 
                    condition += f"firstname LIKE '%{firstname}%'"
            if lastname:
                if condition:
                    condition += f" and lastname LIKE '%{lastname}%'"
                else:
                    condition += f"lastname LIKE '%{lastname}%'"
            if address:
                if condition:
                    condition += f" and address LIKE '%{address}%'"
                else:
                    condition += f"address LIKE '%{address}%'"
            if phone:
                if condition:
                    condition += f" and phone LIKE '%{phone}%'"
                else:
                    condition += f"phone LIKE '%{phone}%'"
        
        if condition:
            query = f"SELECT * FROM customer WHERE {condition};"
        else:
            query = f"SELECT * FROM customer;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()
