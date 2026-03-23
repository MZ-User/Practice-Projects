from DB_Manager import DB_Manger
Db = DB_Manger()
from Interface import Welcome
interface = Welcome()

class Account_Functions:
 def __init__(self):
  pass

 #---------------Take Registeration Data from User---------------
 def Registeration_Data_Taker(self):
  interface.Logo()
  Name = input('Enter your Name: ')
  Email = input('Enter your E-Mail: ')
  Username = input('Set your Username: ')
  Password = input('Set your Password: ')
  Cpaswd = input('Confirm your Password: ')
  while (Cpaswd != Password):
   Cpaswd = input('Password not match! Confirm Password Again: ')
  Registeration_Data = {'name': Name, 'email': Email, 'username': Username, 'password': Password}
  return Registeration_Data

 #---------------Save a Unique User's Data in Database---------------
 def Registeror_Function(self):
   Registeration_Data = self.Registeration_Data_Taker()
   Table_Creator_Query = '''CREATE TABLE IF NOT EXISTS Registered_Users_Data(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   email TEXT,
   username TEXT,
   password TEXT
   )'''
   DB_Existance = Db.Database_Finder()
   if DB_Existance == False:
    Db.DB_Creator()
    Db.Table_Creator(Table_Creator_Query)
   Query_for_Data_Saver = '''INSERT INTO Registered_Users_Data (name, email, username, password) VALUES (?, ?, ?, ?)''', (Registeration_Data['name'], Registeration_Data['email'], Registeration_Data['username'], Registeration_Data['password'])
   Db.Data_Saver(Query_for_Data_Saver)
   print('\nAccount Created Sucessfully\n\nPlease Login to your Account\n\n')
   self.Login_Function()

 #---------------Take Login Data from User---------------
 def Login_Data_Taker(self):
  username = input('Enter your Username: ')
  password = input('Enter your Password: ')
  return username, password

 #---------------Import All Registered Users Data from Database---------------
 def Database_Holder(self):
  Data =Db.All_Data()
  return Data

 #---------------Detect if User Exists and Match Login Credentials---------------
 def Login_Data_Matcher(self, data):
  All_Users_Data = self.Database_Holder()
  Matching = ''
  for i in All_Users_Data:
   if (i[3] == data[0] and i[4] == data[1]):
    Matching = True
    return Matching
   else:
    Matching =  False
  return Matching

  #---------------Take Login Credentials and Matach with Registered User's Data from Database---------------
 def Login_Function(self):
  Login_Data = self.Login_Data_Taker()
  Matching_Result = self.Login_Data_Matcher(Login_Data)
  i = 0
  while i < 1:
   if Matching_Result == True:
    i = 2
    print('\nLogin Sucessfully\n')
    return
   else:
    print('\nInvalid Credentials! Please Try Again\n')
    Login_Data = self.Login_Data_Taker()
    Matching_Result = self.Login_Data_Matcher(Login_Data)
