import os
from global_constants import *
from general import logo as L
from security import security as S

class share:
    def __init__(self):
        pass

    def start(self):
        S(REQUITRTEMENTS_FILE).check() # verify the installations of omodules listed in "requirements.txt"

        # show the logo
        L(COLORS_FILE, SETTINGS_FILE).print_logo()


share().start()