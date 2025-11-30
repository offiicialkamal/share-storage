from art import text2art
import random
import time

class logo:
    def __init__(self, colors, logo_settings):
        self.__colors = colors
        self.__logo_settings = logo_settings.get("logo")
        self.__font = self.__logo_settings.get("font")

    def get_color(self):
        if self.__logo_settings.get("color")
        color = self.__colors.get(random.choice(self.__colors))
        return color

    def generate_logo(self, s=None):
        art = text2art(s, self.__font) if s else text2art(self.__logo_settings.get("text"), self.__font)
        return art

    def print_logo(self, banner: str):
        lines = banner.splitlines()
        for line in lines:
            for ch in line:
                print(ch, end="")
                time.sleep(self.__delay/35)
            print()
        return True

# a = logo()
# a.print_logo(a.generate_logo("kamal"))
