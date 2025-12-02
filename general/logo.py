import time
import random
from art import text2art
from file_handlers import read_json
from customs import show

class logo:
    def __init__(self, colors_file_path : str, settings_file_path : str):
        self.__colors = read_json(colors_file_path)
        self.__logo_settings = read_json(settings_file_path).get("logo")
        self.__font = self.__logo_settings.get("font")

    def get_color(self):
        color = ""
        if self.__logo_settings.get("color"):
            # print(type(self.__colors))
            color = self.__colors.get(random.choice(list(self.__colors.keys())))
        return color

    def generate_logo(self, s=None):
        art = text2art(s, self.__font) if s else text2art(self.__logo_settings.get("text"), self.__font)
        return art

    def print_logo(self, banner = None):
        lenth = None
        lines = banner.splitlines() if banner else self.generate_logo().splitlines()
        for line in lines:
            if not lenth:
                lenth = len(line)
                print("<< " + "=" * lenth + " >>")
            lenth = len(line)
            color = self.get_color()
            show(color + "   " + line)
        # print()
        # print("=" * lenth)
        # print("=" * lenth)

        return lenth

# a = logo()
# a.print_logo(a.generate_logo("kamal"))


[
    [
    [
        [1,2],
        [1,2]
    ],
     [
        [1,2],
        [1,2]
    ]
],
[
    [
        [1,2],
        [1,2]
    ],
     [
        [1,2],
        [1,2]
    ]
]
]

