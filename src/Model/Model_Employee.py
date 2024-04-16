import mysql.connector

class Model_Employee:
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
    
    def selectRandom(self, position):
        self.open()
        query = f"""SELECT employeeID FROM Employee WHERE position = '{position}'
                    ORDER BY RAND()
                    LIMIT 1;"""
        
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

    
    def checkExist(self, employeeID):
        self.open()
        query = f"""SELECT employeeID FROM employee WHERE employeeID LIKE '{employeeID}';"""

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
    
    def add(self, employeeID, firstname, lastname, DOB, position, salary):
        self.open()
        query = f"""INSERT INTO employee (employeeID, firstname, lastname, DOB, position, salary)
                    VALUES ('{employeeID}', '{firstname}', '{lastname}', '{DOB}', '{position}', {salary});"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def update(self, employeeID, firstname, lastname, DOB, position, salary):
        self.open()
        query = f"""UPDATE employee 
                    SET firstname = '{firstname}', lastname = '{lastname}', DOB = '{DOB}', position = '{position}', salary = {salary}
                    WHERE employeeID = '{employeeID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def delete(self, employeeID):
        self.open()
        query = f"DELETE FROM employee WHERE employeeID = '{employeeID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def search(self, employeeID=None, firstname=None, lastname=None, DOB=None, position=None, salary=None):
        self.open()

        condition = ""
        if employeeID:
            condition += f"employeeID LIKE '%{employeeID}%'"
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
            if DOB:
                if condition:
                    condition += f" and DOB >= '{DOB}'"
                else:
                    condition += f"DOB >= '{DOB}'"
            if position:
                if condition:
                    condition += f" and position LIKE '%{position}%'"
                else:
                    condition += f"position LIKE '%{position}%'"
            if salary:
                if condition:
                    condition += f" and salary LIKE '%{salary}%'"
                else:
                    condition += f"salary LIKE '%{salary}%'"
        
        if condition:
            query = f"SELECT * FROM employee WHERE {condition};"
        else:
            query = f"SELECT * FROM employee;"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()
