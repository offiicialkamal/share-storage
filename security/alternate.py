import time
from file_handlers import read_text
from customs import show
from global_constants import ALTERNATE_LOGO_PATH, 

class alternate_option():
    def __init__(self):
        pass

    def start():
        pass

    def show_other_opetion(self):
        time.sleep(2)
        show("their was an error please select one of following")
        self.clear()
        choice = input("Enter Your Choice")

    def print_alternate_banner(self):
        help_banner = read_text().splitlines()
        for line in help_banner:
            show(line)