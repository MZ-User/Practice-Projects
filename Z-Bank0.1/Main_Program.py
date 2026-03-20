import time
import os
import sys
import json
os.system("cls" if os.name == "nt" else "clear")

#           Welcome
def Welcome():
 time.sleep(1)
 print('Welcome to "Z Bank Limited"')
 time.sleep(2)
 os.system("cls" if os.name == "nt" else "clear")

#           Options for User
def Options():
 print('---Z Bank Limited---\n1. Register\n2. Login\n')
 R_L = int(input('Enter Number from above options: '))
 while (R_L != 1 and R_L != 2):
  R_L = int(input('Invalid Value! Please enter 1 or 2 Value: '))
 os.system("cls" if os.name == "nt" else "clear")
 return R_L

#               If json File not Exist
#           First Time Registeration
def Registeration_Data_Taker():
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

#             Data Saver
def First_Registeration_Data_Saver(registeration_data):
 with open('Database.json', 'w') as DB:
  json.dump(registeration_data, DB)
 print('\nAccount Created Sucessfully\n')
 return

#            Showing Options Again
def Show_Options_Again():
 Returned_R_L = Options()
 return Returned_R_L

#            if json file Exists

def Check_Existing_Users_in_Json(Usrnem, Mail):
 a = ''
 b = ''
 with open('Database.json', 'r') as DB:
  All_Users_Data = json.load(DB)
 for i in All_Users_Data:
  while True:
   if (i['username'] != Usrnem):
    if (i['email'] != Mail):
     break
    else:
     print('\nEmail already in use\n')
     b = 'Email already in use'
     break
   else:
    print('\nUsername already in use\n')
    a = 'Username already in use'
    if i['email'] != Mail:
     pass
    else:
     print('\nEmail already in use\n')
     b = 'Email already in use'
    break
 return a, b

#            Login Credentials Matcher
def Login_Credentials_Matcher(a, b):
 with open('Database.json', 'r') as users:
  All_Users = json.load(users)
 c = ''
 d = ''
 for i in All_Users:
  while True:
   if i['username'] == a:
    a = ''
    if i['password'] == b:
     print('\nLogin Sucessfully\n')
     c = ''
     d = ''
     return c, d
    else:
     print('\nWrong Password\n')
     c = 'Wrong Password'
     return c, d
   else:
    c = '\nUsername Not Exists\n'
    print('\n\n')
    break
 return c, d

#           Login When Json is Available
def Login_When_Json():
 Username = input('Enter your Username: ')
 Password = input('Enter your Password: ')
 return Username, Password

Welcome()
if not os.path.exists('Database.json'):
 R_L = Options()
 while True:
  if R_L == 1:
   Registeration_Data_Dictionary = Registeration_Data_Taker()
   First_Registeration_Data_Saver(Registeration_Data_Dictionary)
   break
  else:
   print('\nPlease Register an Account before Login\n')
   R_L = Show_Options_Again()
else:
 R_L = Options()
 if R_L == 1:
  Registeration_Data_Taker_Result = Registeration_Data_Taker()
  Registeration_Data = Registeration_Data_Taker_Result[0]
  c = Check_Existing_Users_in_Json(Registeration_Data['username'], Registeration_Data['email'])
  while True:
   if (c[0] == '' and c[1] == ''):
    with open('Database.json', 'r') as DB:
     previous_data = json.load(DB)
    previous_data.append(Registeration_Data)
    with open('Database.json', 'w') as db:
     json.dump(previous_data, db)
    print('\nAccount Created Sucessfully\n')
    break
   else:
    Registeration_Data_Taker_Result = Registeration_Data_Taker()
    Registeration_Data = Registeration_Data_Taker_Result[0]
    c = Check_Existing_Users_in_Json(Registeration_Data['username'], Registeration_Data['email'])
 else:
  Logs = Login_When_Json()
  Matching_Result = Login_Credentials_Matcher(Logs[0], Logs[1])
  while True:
   if (Matching_Result[0] == '' and Matching_Result[1] == ''):
    break
   else:
    Logs = Login_When_Json()
    Matching_Result = Login_Credentials_Matcher(Logs[0], Logs[1])