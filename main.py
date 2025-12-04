import os
import time
import sys
from threading import Thread
import webbrowser as wb
from core import main_thread, secondary_thread
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
            print("05 Exit")
            print("<< " + "=" * lenth + " >>")
            choice = int(input("Enter Your Choice : "))
            print("<< " + "=" * lenth + " >>")
            return choice
        except Exception as e:
            print("Unexpected Input Please choose one of the given option")
            time.sleep(3)
            self.start()
    
    def run_choice(self, choice: int):
        if choice == 1:
            main_thread().start()
            secondary_thread(BINARY_PATH[0], LOCAL_PORT[0]).start()
        elif choice == 2:main_thread().start()
        elif choice == 3:wb.open("https://github.com/offiicialkamal/share-storage/blob/main/readme.md")
        elif choice == 4:wb.open("https://github.com/offiicialkamal/share-storage.git")
        elif choice == 5:sys.exit()
        else:print("\nFollow us on github");time.sleep(2);wb.open("https://github.com/offiicialkamal")

    def clear(self):
        os.system('clear')



share().start()