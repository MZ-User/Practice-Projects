import time
import os
from Interface import Welcome
Welcome_Object =  Welcome()
from Interface import Extra_Interfaces
Extras = Extra_Interfaces()
from DB_Manager import DB_Manger
db = DB_Manger()
from Accountant import Account_Functions
accountant = Account_Functions()

class All_Functions:
 def __init__(self):
  pass

 #----------Say Welcome to User----------
 def Say_Welcome(self):
  Welcome_Object.Welcome_Shower()
  return

 #           Show Options to User
 def Options(self):
  Choice = Extras.options_for_user()
  return Choice

 #          Check if Database(db) file exist or not
 def DB_Existance_Detector(self):
  Existance = db.Database_Finder()
  return Existance

All_Function = All_Functions()
All_Function.Say_Welcome()
Choice = All_Function.Options()
DB_Existance = All_Function.DB_Existance_Detector()

if DB_Existance == False:
 while True:
  if Choice == 1:
    accountant.Registeror_Function()
    break
  else:
   print('\n\nPlease Register an Account before Login\n')
   Choice = All_Function.Options()
else:
 if Choice == 1:
  User_Data = accountant.Registeror_Function()
 else:
  accountant.Login_Function()