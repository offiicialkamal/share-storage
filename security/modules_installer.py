import os
import time
import importlib
import subprocess
from customs import show
from file_handlers import read_text
from customs import show
from global_constants import ALTERNATE_LOGO_PATH
from .cloudFlare_installer import cloudeflared_installer as cloudFlared

# cat /etc/os-release it works on all systems

cloudflared_install = {
    "windows": "winget install Cloudflare.cloudflared",
    "macos": "brew install cloudflared",
    "debian": "sudo apt install cloudflared",
    "ubuntu": "sudo apt install cloudflared",
    "arch": "sudo pacman -S cloudflared",
    "fedora": "sudo dnf install cloudflared",
    "redhat": "sudo dnf install cloudflared",
    "alpine": "apk add cloudflared",
    "generic_linux_binary": (
        "curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/"
        "cloudflared-linux-amd64 -o cloudflared && "
        "chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
    ),
}

class cloudflared:
    """"verifies the installations of cloudeflared module"""
    def __init__():
        pass
    
    def mac():
        os.system()

class security:
    """ Verifies the installlations of all the python pip packages listed in the requirements.txt file"""
    def __init__(self, requirements_file):
        self.__requirements_file = requirements_file
    
    def check(self):
        try:
            # import the all python packages listed inside the requirements file
            for module in read_text(self.__requirements_file).splitlines():
                module_name = module.split("=")[0]
                globals()[module_name] = importlib.import_module(module_name)
                # globals()["cloudflared"] = importlib.import_module("cloudflared")
                # print("all modules installed sucessfully")
            ## means all mdules are avilable
            ## now check the cloudflared
            cloudFlared().ensure_cloudflared_binary_and_set_path_to_global()
            
        except Exception as e:
            print("modules aare missing ", e)
            self.install()

    def install(self):
        try:
            # for module in read_text().splitlines():
            #     os.system(f"pip install {module}")
            subprocess.run(["pip", "install", "-r", "requirements.txt"])
        except Exception as e:
            print(e)
            
    def clear(self):
        os.system("clear")
