import mysql.connector

class Model_ProductDetail:
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

    def addLaptop(self, productID, MFG, RAM, ROM, CPU, VGA, keyboard, screen, OS, size, pin, type):
        self.open()
        query = f"""INSERT INTO productdetail (productID, MFG, RAM, ROM, CPU, VGA, keyboard, screen, OS, size, pin, type)
                    VALUES ('{productID}', '{MFG}', '{RAM}', '{ROM}', '{CPU}', '{VGA}', '{keyboard}', '{screen}', '{OS}', '{size}', '{pin}', '{type}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def addRAM(self, productID, MFG, capacity, type, SPDspeed, CL, size):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, capacity, type, SPDspeed, CL, size)
                    VALUES ('{productID}', '{MFG}', '{capacity}', '{type}', '{SPDspeed}', '{CL}', '{size}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def addROM(self, productID, MFG, capacity, type, writeSpeed, readSpeed):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, capacity, type, writeSpeed, readSpeed)
                    VALUES ('{productID}', '{MFG}', '{capacity}', '{type}', '{writeSpeed}', '{readSpeed}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def addCPU(self, productID, MFG, cores, threads, series):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, cores, threads, series)
                    VALUES ('{productID}', '{MFG}', '{cores}', '{threads}', '{series}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def addVGA(self, productID, MFG, cores, GPUclock, size):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, cores, GPUclock, size)
                    VALUES ('{productID}', '{MFG}', '{cores}', '{GPUclock}', '{size}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def addKeyboard(self, productID, MFG, layout, size, LED, keycap, switch, pin, hotswap):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, layout, size, LED, keycap, switch, pin, hotswap)
                    VALUES ('{productID}', '{MFG}', '{layout}', '{size}', '{LED}', '{keycap}', '{switch}', '{pin}', '{hotswap}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def addScreen(self, productID, MFG, scan, size, panel, resolution):
        self.open()
        query = f"""INSERT INTO importdetail (productID, MFG, scan, size, panel, resolution)
                    VALUES ('{productID}', '{MFG}', '{scan}', '{size}', '{panel}', '{resolution}');"""

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def updateLaptop(self, productID, MFG, RAM, ROM, CPU, VGA, keyboard, screen, OS, size, pin, type):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if RAM:
            if condition:
                condition += f", RAM = '{RAM}'"
            else:
                condition += f"RAM = '{RAM}'"
        if ROM:
            if condition:
                condition += f", ROM = '{ROM}'"
            else:
                condition += f"ROM = '{ROM}'"
        if CPU:
            if condition:
                condition += f", CPU = '{CPU}'"
            else:
                condition += f"CPU = '{CPU}'"
        if VGA:
            if condition:
                condition += f", VGA = '{VGA}'"
            else:
                condition += f"VGA = '{VGA}'"
        if keyboard:
            if condition:
                condition += f", keyboard = '{keyboard}'"
            else:
                condition += f"keyboard = '{keyboard}'"
        if screen:
            if condition:
                condition += f", screen = '{screen}'"
            else:
                condition += f"screen = '{screen}'"
        if OS:
            if condition:
                condition += f", OS = '{OS}'"
            else:
                condition += f"OS = '{OS}'"
        if size:
            if condition:
                condition += f", size = '{size}'"
            else:
                condition += f"size = '{size}'"
        if pin:
            if condition:
                condition += f", pin = '{pin}'"
            else:
                condition += f"pin = '{pin}'"
        if type:
            if condition:
                condition += f", type = '{type}'"
            else:
                condition += f"type = '{type}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def updateRAM(self, productID, MFG, capacity, type, SPDspeed, CL, size):
        self.open()

        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if capacity:
            if condition:
                condition += f", capacity = '{capacity}'"
            else:
                condition += f"capacity = '{capacity}'"
        if SPDspeed:
            if condition:
                condition += f", SPDspeed = '{SPDspeed}'"
            else:
                condition += f"SPDspeed = '{SPDspeed}'"
        if CL:
            if condition:
                condition += f", CL = '{CL}'"
            else:
                condition += f"CL = '{CL}'"
        if size:
            if condition:
                condition += f", size = '{size}'"
            else:
                condition += f"size = '{size}'"
        if type:
            if condition:
                condition += f", type = '{type}'"
            else:
                condition += f"type = '{type}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def updateROM(self, productID, MFG, capacity, type, writeSpeed, readSpeed):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if capacity:
            if condition:
                condition += f", capacity = '{capacity}'"
            else:
                condition += f"capacity = '{capacity}'"
        if writeSpeed:
            if condition:
                condition += f", writeSpeed = '{writeSpeed}'"
            else:
                condition += f"writeSpeed = '{writeSpeed}'"
        if readSpeed:
            if condition:
                condition += f", readSpeed = '{readSpeed}'"
            else:
                condition += f"readSpeed = '{readSpeed}'"
        if type:
            if condition:
                condition += f", type = '{type}'"
            else:
                condition += f"type = '{type}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def updateCPU(self, productID, MFG, cores, threads, series):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if cores:
            if condition:
                condition += f", cores = '{cores}'"
            else:
                condition += f"cores = '{cores}'"
        if threads:
            if condition:
                condition += f", threads = '{threads}'"
            else:
                condition += f"threads = '{threads}'"
        if series:
            if condition:
                condition += f", series = '{series}'"
            else:
                condition += f"series = '{series}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
        
    def updateVGA(self, productID, MFG, cores, GPUclock, size):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if cores:
            if condition:
                condition += f", cores = '{cores}'"
            else:
                condition += f"cores = '{cores}'"
        if GPUclock:
            if condition:
                condition += f", GPUclock = '{GPUclock}'"
            else:
                condition += f"GPUclock = '{GPUclock}'"
        if size:
            if condition:
                condition += f", size = '{size}'"
            else:
                condition += f"size = '{size}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def updateKeyboard(self, productID, MFG, layout, size, LED, keycap, switch, pin, hotswap):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if layout:
            if condition:
                condition += f", layout = '{layout}'"
            else:
                condition += f"layout = '{layout}'"
        if LED:
            if condition:
                condition += f", LED = '{LED}'"
            else:
                condition += f"LED = '{LED}'"
        if size:
            if condition:
                condition += f", size = '{size}'"
            else:
                condition += f"size = '{size}'"
        if keycap:
            if condition:
                condition += f", keycap = '{keycap}'"
            else:
                condition += f"keycap = '{keycap}'"
        if switch:
            if condition:
                condition += f", switch = '{switch}'"
            else:
                condition += f"switch = '{switch}'"
        if pin:
            if condition:
                condition += f", pin = '{pin}'"
            else:
                condition += f"pin = '{pin}'"
        if hotswap:
            if condition:
                condition += f", hotswap = '{hotswap}'"
            else:
                condition += f"hotswap = '{hotswap}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()

    def updateScreen(self, productID, MFG, scan, size, panel, resolution):
        self.open()
        
        condition = ""
        if MFG:
            condition += f" MFG = '{MFG}'"
        if scan:
            if condition:
                condition += f", scan = '{scan}'"
            else:
                condition += f"scan = '{scan}'"
        if panel:
            if condition:
                condition += f", panel = '{panel}'"
            else:
                condition += f"panel = '{panel}'"
        if size:
            if condition:
                condition += f", size = '{size}'"
            else:
                condition += f"size = '{size}'"
        if resolution:
            if condition:
                condition += f", resolution = '{resolution}'"
            else:
                condition += f"resolution = '{resolution}'"
        
        query = f"""UPDATE productdetail SET {condition} 
                    WHERE productID = '{productID}';"""
        
        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()
    
    def search(self, productID):
        self.open()

        query = f"SELECT * FROM productdetail WHERE productID = '{productID}';"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.con.close()

    def delete(self, productID):
        self.open()
        query = f"DELETE FROM productdetail WHERE productID = '{productID}';"

        try:
            self.cursor.execute(query)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self.con.close()