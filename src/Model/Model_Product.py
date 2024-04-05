import mysql.connector

class Model_Product:
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
    
    def checkExist(self, productID):
        self.open()
        query = f"""SELECT productID FROM product WHERE productID LIKE '{productID}';"""

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
    
    def add(self, productID, supplierName, productName, type, quantity, warrantyTime, price):
        self.open()
        query = f"""INSERT INTO product (productID, supplierName, productName, type, quantity, warrantyTime, price)
                    VALUES ('{productID}', '{supplierName}', '{productName}', '{type}', '{quantity}', '{warrantyTime}', {price} * 1.3);"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, productID, productName, warrantyTime, price):
        self.open()
        query = f"""UPDATE product 
                    SET productName = '{productName}', warrantyTime = '{warrantyTime}', price = {price}
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def increaseQuantity(self, productID, value, price=None):
        self.open()
        query = f"""UPDATE product 
                    SET quantity = quantity + {value}, price = {price} * 1.3
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def decreaseQuantity(self, productID, value):
        self.open()
        query = f"""UPDATE product 
                    SET quantity = quantity - {value}
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, productID):
        self.open()
        query = f"DELETE FROM product WHERE productID = '{productID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, productID=None, supplierName=None, productName=None, type=None, quantity=None, warrantyTime=None, price=None):
        self.open()

        condition = ""
        if productID:
            condition += f"productID LIKE '%{productID}%'"
        else:
            if supplierName:
                if condition:
                    condition += f" and supplierName LIKE '%{supplierName}%'"
                else: 
                    condition += f"supplierName LIKE '%{supplierName}%'"
            if productName:
                if condition:
                    condition += f" and productName LIKE '%{productName}%'"
                else: 
                    condition += f"productName LIKE '%{productName}%'"
            if type:
                if condition:
                    condition += f" and type LIKE '%{type}%'"
                else:
                    condition += f"type LIKE '%{type}%'"
            if quantity:
                if condition:
                    condition += f" and quantity LIKE '%{quantity}%'"
                else:
                    condition += f"quantity LIKE '%{quantity}%'"
            if warrantyTime:
                if condition:
                    condition += f" and warrantyTime LIKE '%{warrantyTime}%'"
                else:
                    condition += f"warrantyTime LIKE '%{warrantyTime}%'"
            if price:
                if condition:
                    condition += f" and price LIKE '%{price}%'"
                else:
                    condition += f"price LIKE '%{price}%'"
        
        if condition:
            query = f"SELECT * FROM product WHERE {condition};"
        else:
            query = f"SELECT * FROM product;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()
