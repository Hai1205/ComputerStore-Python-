import mysql.connector

class Model_Account:
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
    
    def checkExist(self, username):
        self.open()
        query = f"""SELECT username FROM account WHERE username LIKE '{username}';"""

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

    def signIn(self, username, password):
        self.open()
        query = f"SELECT customerID FROM account WHERE username LIKE '{username}' AND password LIKE '{password}'"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.con.commit()
            return result
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def signUp(self, username, password, customerID):
        self.open()
        query = f"""INSERT INTO account (customerID, username, password)
                    VALUES ('{customerID}', '{username}', '{password}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, username, password):
        self.open()
        query = f"""UPDATE account SET password = '{password}' WHERE username = '{username}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, username):
        self.open()
        query = f"DELETE FROM account WHERE username = '{username}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, username=None, password=None, customerID=None):
        self.open()

        condition = ""
        if username:
            condition += f"username LIKE '%{username}%'"
        else:
            if password:
                if condition:
                    condition += f" and password LIKE '%{password}%'"
                else: 
                    condition += f"password LIKE '%{password}%'"
            if customerID:
                if condition:
                    condition += f" and customerID LIKE '%{customerID}%'"
                else:
                    condition += f"customerID LIKE '%{customerID}%'"
        
        if condition:
            query = f"SELECT * FROM account WHERE {condition};"
        else:
            query = f"SELECT * FROM account;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()