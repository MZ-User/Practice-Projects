import os
import time
import sys

class Welcome:
    def __init__(self):
        # if os.name == 'nt':
        #     os.system('')
        pass

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def togle_cursor(self, show=True):
        if show:
            sys.stdout.write('\033[?25h')
        else:
            sys.stdout.write('\033[?25l')
        sys.stdout.flush()

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
     time.sleep(1.2)
     self.loading_dot(6, 'Starting App')
     return
