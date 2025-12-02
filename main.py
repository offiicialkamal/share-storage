import os
import time
from global_constants import *
from general import logo as L
from security import security as S

class share:
    def __init__(self):
        pass

    def start(self):
        self.clear()
        S(REQUITRTEMENTS_FILE).check() # verify the installations of omodules listed in "requirements.txt"
        lenth = L(COLORS_FILE, SETTINGS_FILE).print_logo() # # show the logo
        
        self.run_choice(self.get_choice(lenth))

    def get_choice(self, lenth):
        try:
            print("<< " + "=" * lenth + " >>")
            print("01 UBIVERSAL LINK")
            print("02 LOCAL LINK")
            print("03 DOCUMENTATION")
            print("04 SEE SOURCE CODE")
            print("<< " + "=" * lenth + " >>")
            choice = int(input("Enter Your Choice : "))
            print("<< " + "=" * lenth + " >>")
            return choice
        except Exception as e:
            print("Unexpected Input Please choose one of the given option")
            time.sleep(3)
            self.start()
    
    def run_choice(choice: int):
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            pass

    def clear(self):
        os.system('clear')



share().start()