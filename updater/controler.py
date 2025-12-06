import os
import json
import subprocess
import requests
from general import logo as L
from global_constants import *
from file_handlers import read_json
from customs import show
import webbrowser as wb
import sys
import time
import re

class updates:
    def __init__(self):
        self.__logo_width = 0
        self.__global_settings = None
        self.__global_url = "https://raw.githubusercontent.com/offiicialkamal/share-storage/refs/heads/main/"

    def check(self):
        # self.__global_settings = self.get_global_version(self.__global_url + "essensials/settings.json")
        self.__global_settings = self.get_global_file(self.__global_url + "essensials/settings.json")
        self.__global_version = self.get_global_version()
        local_version = self.get_local_version()

        print("if statement executed")
        print(self.__global_settings)
        print(self.__global_version)
        print(local_version)
        
        if not self.__global_settings:return
        
        if not local_version == self.__global_version:
            print(self.__global_settings)
            update_settings = self.__global_settings.get("update")
            print(update_settings)
            auto_update_suggetion, force_updates = update_settings.values()
            
            if force_updates:self.update()
            elif auto_update_suggetion:
                self.show_update_logo()
                self.show_options()
                choice = self.get_choice()
                if choice:self.handle_choice(choice)
            else:sys.exit()
        else:return
        
    def update(self):
        # imlement the update process hear
        show(" UPDATE IS IN PROGRESS PLEASE WAIT FOR SOME ")
        r = str(subprocess.run(["git", "-version"], text=True, capture_output=True))
        pattern = r"^git version \d+\.\d+\.\d+.*\n?$"

        is_installed = True if re.match(pattern, r) else False
        if is_installed:os.system("git pull")
        else: print("YOU DON'T HAVE GIT INSTALLED PLEASE INSTALL THE GIT TO UPDATE THE TOOL")
        sys.exit()

    def show_update_logo(self):
        os.system("clear")
        logo_class = L(COLORS_FILE, SETTINGS_FILE)
        logo = logo_class.generate_logo("UPDATE") 
        self.__logo_width = logo_class.print_logo(logo)
        time.sleep(3)

    def show_options(self):
        print("   01 UPDATE")
        print("   02 WHATS NEW")
        print("   03 UPDATE LATER")
        print("   04 SEE SOURCE CODE")
        print("   05 Exit")
        print("<< " + "=" * self.__logo_width + " >>")

    def get_choice(self):
        try:
            choice = int(input("ENTER YOUR CHOICR : "))
            return choice
        except Exception as _:
            show("please choose an valid option ")
            self.show_update_logo()

    def handle_choice(self, choice):
        if choice == 1:self.update()
        elif choice == 2:wb.open("https://github.com/offiicialkamal/share-storage/blob/main/changelogs.md")
        elif choice == 3:return
        elif choice == 4:wb.open("https://github.com/offiicialkamal/share-storage.git")
        elif choice == 5:sys.exit()
    
    def get_global_file(self, url, silent = True):
        try:
            return requests.get(url).json()
        except Exception as e:
            if not silent: print(e)
            return None

    def get_global_version(self):
        global_version = None
        return self.get_global_file(self.__global_url + "tool.json").get("version")
    
    def get_local_version(self):
        local_file_url = HOME_DIR + "tool.json"
        return read_json(local_file_url).get("version")

