import os
import json
import requests
from general import logo as L
from global_constants import *
from file_handlers import read_json



class updator:
    def __init__(self):
        self.__logo_width = 0
        self.__global_settings = None
        self.__global_url = "https://raw.githubusercontent.com/offiicialkamal/share-storage/refs/heads/main/"




    def check(self):
        self.__global_settings = self.get_global_settings(self.__global_url + "essensials/settings.json")
        
        if not (self.get_local_version() == self.get_global_version()):
            if not self.__global_settings:
                return
            else:
                update_settings = self.__global_settings.get("update")
                force_updates, auto_update_suggetion = update_settings.values() 
                
                if auto_update_suggetion:
                    self.show_update_logo()
                    self.show_options()
                    self.handle_choice(self.get_choice())

                elif force_updates:
                    self.update()
        else:
            return
        
    def update(self):
        pass

    def show_update_logo(self):
        os.system("clear")
        logo_class = L(COLORS_FILE, SETTINGS_FILE)
        logo = logo_class.generate_logo("UPDATE") 
        self.__logo_width = logo_class.print_logo(logo)
        

    def show_options():
        pass

    def get_choice(self):
        pass

    def handle_choice(self):
        pass
    
    def get_global_file(self, url, silent = True):
        try:
            return requests.get(url).json
        except Exception as e:
            if not silent: print(e)
            return None

    def get_global_version(self):
        global_version = None
        content = self.get_global_file(self.__global_url + "tool.json").json
        if content:global_version = content.get("version")
        return global_version
    
    def get_local_version(self):
        local_file_url = HOME_DIR + "tool.json"
        content = read_json(local_file_url)
        if content:local_version = content.get("version")
        return local_version

