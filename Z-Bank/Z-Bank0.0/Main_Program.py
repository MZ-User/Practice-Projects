import time
import os
import sys
os.system("cls" if os.name == "nt" else "clear")
#time.sleep(2)
#print('Welcome to "Z Bank Limited"')
#time.sleep(4)
#os.system("cls" if os.name == "nt" else "clear")

#           Options for User
def Options():
 print('---Z Bank Limited---\n')
 print('1. Register')
 print('2. Login\n')
 R_L = int(input('Enter Number from above options: '))
 while (R_L != 1 and R_L != 2):
  R_L = int(input('Invalid Value! Please enter 1 or 2 Value: '))
 os.system("cls" if os.name == "nt" else "clear")
 return R_L

#           First Time Registeration
def firstRegisteration():
 print('---Z Bank Limited---')
 Name = input('Enter your Name: ')
 Email = input('Enter your E-Mail: ')
 Username = input('Set your Username: ')
 Password = input('Set your Password: ')
 Cpaswd = input('Confirm your Password: ')
 while (Cpaswd != Password):
  Cpaswd = input('Password not match! Confirm Password Again: ')
 #  this remove all spaces tabs and enters form user name
 #userName = ''.join(Name.split())
 credentials_file = open('User_Credentials.py', 'w')
 credentials_file.write(f"class User_Registeraion_Info:\n def __init__(self, N, E, U, P):\n  self.name = N\n  self.email = E\n  self.username = U\n  self.password = P\n\ndef user_counter(current_count):\n return current_count + 1\ndef user_name_maker(userCount):\n a = str(userCount)\n b = 'User' + a\n return b\n\nAll_Users_Data = dict('')\n\nuser_count = 0\n\nGenerated_Name = user_name_maker(user_count)\n\nAll_Users_Data[Generated_Name] = User_Registeraion_Info('{Name}','{Email}','{Username}','{Password}')")
 credentials_file.close()
 print('Account Created Successfully')

#           First Time Login
def firstLogin():
 print('\n')
 Username = input('Enter your Username: ')
 Password = input('Enter your Password: ')
 print('\nAccount not Exists! Please Register an account before Login\n')

#            Existing Users Detactor
def Existing_Users_Detactor(Usrnem, Mail):
 import User_Credentials
 a = ''
 b = ''
 for i in User_Credentials.All_Users_Data:
  while True:
   if (User_Credentials.All_Users_Data[i].username != Usrnem):
    if (User_Credentials.All_Users_Data[i].email != Mail):
     break
    else:
     print('Email already in use')
     b = 'Email already in use'
     break
   else:
    print('Username already in use')
    a = 'Username already in use'
    if User_Credentials.All_Users_Data[i].email != Mail:
     pass
    else:
     print('Email already in use')
     b = 'Email already in use'
    break
 return a, b

#          Registeration After First Registeration
def After_firstRegisteration():
 print('---Z Bank Limited---')
 Name = input('Enter your Name: ')
 Email = input('Enter your E-Mail: ')
 Username = input('Set your Username: ')
 Password = input('Set your Password: ')
 Cpaswd = input('Confirm your Password: ')
 while (Cpaswd != Password):
  Cpaswd = input('Password not match! Confirm Password Again: ')
 #  this remove all spaces tabs and enters form user name
 #class_name = ''.join(Name.split())
 matching = Existing_Users_Detactor(Username, Email)
 if (matching[0] == '' and matching[1] == ''):
  credentials_file = open('User_Credentials.py', 'a')
  credentials_file.write(f"\n\nuser_count = user_counter(user_count)\n\nGenerated_Name = user_name_maker(user_count)\nAll_Users_Data[Generated_Name] = User_Registeraion_Info('{Name}', '{Email}', '{Username}', '{Password}')")
  credentials_file.close()
  print('Account Created Successfully')
 else:
  After_firstRegisteration()

#            Login Data Authenticator
def Login_checker(a, b):
 import User_Credentials
 for i in User_Credentials.All_Users_Data:
  while True:
   if User_Credentials.All_Users_Data[i].username == a:
    if User_Credentials.All_Users_Data[i].password == b:
     print('Login Sucessfully')
     return
    else:
     print('Wrong Password')
   else:
    break
 print('Username not Found')
 return

#           Login After First Login
def After_firstLogin():
 Username = input('Enter your Username: ')
 Password = input('Enter your Password: ')
 return Username, Password


if not os.path.exists('User_Credentials.py'):
 R_L = Options()
 while True:
  if R_L == 1:
   firstRegisteration()
   break
  else:
   firstLogin()
   R_L = Options()
else:
 R_L = Options()
 if R_L == 1:
  After_firstRegisteration()
 else:
  Logs = After_firstLogin()
  Login_checker(Logs[0], Logs[1])