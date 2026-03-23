import time
import os
import json
from Welcome import Welcome
Welcome_Object =  Welcome()

class All_Functions:
 def __init__(self):
  pass

 #----------Say Welcome to User----------
 def Say_Welcome(self):
  Welcome_Object.Welcome_Shower()
  return

 #           Show Options to User
 def Options(self):
  print('\n\n\n---Z Bank Limited---\n\n1. Register\n2. Login\n')
  User_Choice = int(input('Enter Number from above options: '))
  while (User_Choice != 1 and User_Choice != 2):
   User_Choice = int(input('Invalid Value! Please enter 1 or 2 Value: '))
  os.system("cls" if os.name == "nt" else "clear")
  return User_Choice
 
 #          Check if json file exist or not
 def File_Existance_Detector(self):
  if not os.path.exists('Database.json'):
   return ''
  else:
   return 'File Exists'

 def Registeration_Data_Taker(self):
  print('---Z Bank Limited---')
  Name = input('Enter your Name: ')
  Email = input('Enter your E-Mail: ')
  Username = input('Set your Username: ')
  Password = input('Set your Password: ')
  Cpaswd = input('Confirm your Password: ')
  while (Cpaswd != Password):
   Cpaswd = input('Password not match! Confirm Password Again: ')
  Registeration_Data = [{'name': Name, 'email': Email, 'username': Username, 'password': Password}]
  return Registeration_Data

 def Data_Saver(self, data):
  with open('Database.json', 'a') as DB:
   json.dump(data, DB)
  return

 def Login_Data_Taker(self):
  username = input('Enter your Username: ')
  password = input('Enter your Password: ')
  return username, password

 def Database_Holder(self):
  with open('Database.json', 'r') as DB_Data:
   All_Data = json.load(DB_Data)
  return All_Data

 def Login_Data_Matcher(self, data):
  Users_List = self.Database_Holder()
  for i in Users_List:
   if (i['username'] == data[0] and i['password'] == data[1]):
    return ''
   else:
    return 'Already in Use'

 def Login_Function(self):
  Login_Data = self.Login_Data_Taker()
  Matching_Result = self.Login_Data_Matcher(Login_Data)
  i = 0
  while i < 1:
   if Matching_Result == '':
    i = 2
    print('\nLogin Sucessfully')
    return
   else:
    print('\nInvalid Credentials! Please Try Again\n')
    Login_Data = All_Function.Login_Data_Taker()
    Matching_Result = All_Function.Login_Data_Matcher(Login_Data)

 def Unique_Registeration_maker(self):
  User_Data_List = self.Registeration_Data_Taker()
  User_Data = User_Data_List[0]
  All_Users = self.Database_Holder()
  a = ''
  b = ''
  while True:
   for i in All_Users:
    if (i['email'] == User_Data['email'] and i['username'] == User_Data['username']):
     print('\nBoth Email and Username are Already in Use\n')
     a = 'Both Email and Username are Already in Use'
    elif i['email'] == User_Data['email']:
     print('\nEmail Already in Use\n')
     b = 'Email Already in Use'
    elif i['username'] == User_Data['username']:
     print('\nUsername Already in Use\n')
     a = 'Username Already in Use'
    else:
     pass
   if a == '' and b == '':
    Data_List = self.Database_Holder()
    Data_List.append(User_Data)
    with open('Database.json', 'w') as Db:
     json.dump(Data_List, Db)
    print('\nAccount Created Successfuly\n')
    return
   else:
    User_Data_List = self.Registeration_Data_Taker()
    User_Data = User_Data_List[0]

All_Function = All_Functions()
#All_Function.Say_Welcome()
Choice = All_Function.Options()
Json_Existance = All_Function.File_Existance_Detector()
Login_Data = ''

if Json_Existance == '':
 while True:
  if Choice == 1:
   User_Data = All_Function.Registeration_Data_Taker()
   All_Function.Data_Saver(User_Data)
   print('\nAccount Created Sucessfully\n\nPlease Login to your Account\n\n')
   All_Function.Login_Function()
   break
  else:
   print('\n\nPlease Register an Account before Login\n')
   Choice = All_Function.Options()
else:
 if Choice == 1:
  User_Data = All_Function.Unique_Registeration_maker()
 else:
  All_Function.Login_Function()




# #            Showing Options Again
# def Show_Options_Again():
#  Returned_R_L = Options()
#  return Returned_R_L

# #            if json file Exists

# def Check_Existing_Users_in_Json(Usrnem, Mail):
#  a = ''
#  b = ''
#  with open('Database.json', 'r') as DB:
#   All_Users_Data = json.load(DB)
#  for i in All_Users_Data:
#   while True:
#    if (i['username'] != Usrnem):
#     if (i['email'] != Mail):
#      break
#     else:
#      print('\nEmail already in use\n')
#      b = 'Email already in use'
#      break
#    else:
#     print('\nUsername already in use\n')
#     a = 'Username already in use'
#     if i['email'] != Mail:
#      pass
#     else:
#      print('\nEmail already in use\n')
#      b = 'Email already in use'
#     break
#  return a, b

# #            Login Credentials Matcher
# def Login_Credentials_Matcher(a, b):
#  with open('Database.json', 'r') as users:
#   All_Users = json.load(users)
#  c = ''
#  d = ''
#  for i in All_Users:
#   while True:
#    if i['username'] == a:
#     a = ''
#     if i['password'] == b:
#      print('\nLogin Sucessfully\n')
#      c = ''
#      d = ''
#      return c, d
#     else:
#      print('\nWrong Password\n')
#      c = 'Wrong Password'
#      return c, d
#    else:
#     c = '\nUsername Not Exists\n'
#     print('\n\n')
#     break
#  return c, d


# Welcome()
# if not os.path.exists('Database.json'):
#  R_L = Options()
#  while True:
#   if R_L == 1:
#    Registeration_Data_Dictionary = Registeration_Data_Taker()
#    First_Registeration_Data_Saver(Registeration_Data_Dictionary)
#    break
#   else:
#    print('\nPlease Register an Account before Login\n')
#    R_L = Show_Options_Again()
# else:
#  R_L = Options()
#  if R_L == 1:
#   Registeration_Data_Taker_Result = Registeration_Data_Taker()
#   Registeration_Data = Registeration_Data_Taker_Result[0]
#   c = Check_Existing_Users_in_Json(Registeration_Data['username'], Registeration_Data['email'])
#   while True:
#    if (c[0] == '' and c[1] == ''):
#     with open('Database.json', 'r') as DB:
#      previous_data = json.load(DB)
#     previous_data.append(Registeration_Data)
#     with open('Database.json', 'w') as db:
#      json.dump(previous_data, db)
#     print('\nAccount Created Sucessfully\n')
#     break
#    else:
#     Registeration_Data_Taker_Result = Registeration_Data_Taker()
#     Registeration_Data = Registeration_Data_Taker_Result[0]
#     c = Check_Existing_Users_in_Json(Registeration_Data['username'], Registeration_Data['email'])
#  else:
#   Logs = Login_When_Json()
#   Matching_Result = Login_Credentials_Matcher(Logs[0], Logs[1])
#   while True:
#    if (Matching_Result[0] == '' and Matching_Result[1] == ''):
#     break
#    else:
#     Logs = Login_When_Json()
#     Matching_Result = Login_Credentials_Matcher(Logs[0], Logs[1])
