import sqlite3
import os

class DB_Manger:
    def __init__(self):
        pass

 #---------------Check if Database Available---------------
    def Database_Finder(self):
     available = False
     if not os.path.exists('Database.db'):
      pass
     else:
      available = True
     return available

 #---------------Create Database---------------
    def DB_Creator(self):
        connection = sqlite3.connect('Database.db')
        cursor = connection.cursor()
        connection.commit()
        connection.close()

 #---------------Create Table in Database---------------    
    def Table_Creator(self, quarey):
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()
        cursor.execute(quarey)
        conn.commit()
        conn.close()

 #---------------Save Date in Database---------------    
    def Data_Saver(self, insert_query):
        conn = sqlite3.connect('Database.db')
        cur = conn.cursor()
        cur.execute(insert_query[0], insert_query[1])
        conn.commit()
        conn.close()

 #---------------Extract All Data from Database---------------
    def All_Data(self):
        conn = sqlite3.connect('Database.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Registered_Users_Data''')
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data
