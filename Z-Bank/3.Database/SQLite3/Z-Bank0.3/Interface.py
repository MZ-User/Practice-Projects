import os
import time
import sys
import sqlite3

class Welcome:
    def __init__(self):
        pass

 #---------------Clear Data from Terminal Screen---------------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

 #---------------Terminal Cursor Hide and Unhide---------------
    def togle_cursor(self, show=True):
        if show:
            sys.stdout.write('\033[?25h')
        else:
            sys.stdout.write('\033[?25l')
        sys.stdout.flush()

 #---------------Loading Like Wheel---------------
    def loading_spin(self, duration, loading_type):
        self.togle_cursor(False)
        chars = ['| ', '/ ', '- ', '\\ ']
        starting_time = time.time()
        i = 0
        while (time.time() - starting_time) < duration:
            print(f'\r{loading_type}  {chars[i%4]}', end='', flush=True)
            time.sleep(0.1)
            i += 1
        self.togle_cursor(True)
        self.clear()

 #---------------Loading Dots---------------
    def loading_dot(self, duration, loading_type):
        self.togle_cursor(False)
        chars = ['.   ', '..  ', '... ', '....']
        starting_time = time.time()
        i = 0
        while (time.time() - starting_time) < duration:
            print(f'\r{loading_type} {chars[i%4]}', end='', flush=True)
            time.sleep(0.4)
            i += 1
        self.togle_cursor(True)
        self.clear()

 #---------------Company Logo---------------
    def Logo(self):
        return '---Z-Bank Limited---'
    
    def Welcome_Shower(self):
     def Welcome_Line():
        print(f'\n\n\nWelcome to {self.Logo()}\n\n')
     self.clear()
     self.loading_spin(3, 'Fetching Data ')
     time.sleep(1)
     Welcome_Line()
     time.sleep(0.7)
     self.loading_spin(1.2, 'Checking internet Connectivity')
     Welcome_Line()
     time.sleep(0.3)
     self.loading_spin(0.8, 'Conneting to Server')
     Welcome_Line()
     self.loading_spin(0.5, 'Importing Files')
     Welcome_Line()
     time.sleep(1)
     self.loading_dot(5, 'Starting App')
     return

class Extra_Interfaces:
    def __init__(self):
       pass

 #---------------Display Options to User---------------
    def options_for_user(self):
     print('\n\n\n---Z Bank Limited---\n\n1. Register\n2. Login\n')
     User_Choice = int(input('Enter Number from above options: '))
     while (User_Choice != 1 and User_Choice != 2):
      User_Choice = int(input('Invalid Value! Please enter 1 or 2 Value: '))
     os.system("cls" if os.name == "nt" else "clear")
     return User_Choice