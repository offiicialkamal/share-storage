import platform
import sys
import os
import requests
import subprocess
import signal
import threading
import re
import webbrowser
from customs import show
import time

class secondary_thread(threading.Thread):
    daemon = True

    def __init__(self, binary_path, local_port):
        super().__init__(daemon=True)
        self.__binary_path = binary_path
        self.__PORT = local_port

    def run(self):
        # first daemon thread reads stdout
        # second daemon thread reads stderr
        command = [
            self.__binary_path,
            "tunnel",
            "--url",
            f"http://localhost:{self.__PORT}",
            "--no-autoupdate"
        ]

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=False,

        )

        t1 = threading.Thread(
            target=self.stream_reader,
            args=(process.stdout, self.on_stdout),
            daemon=True
        )

        t2 = threading.Thread(
            target=self.stream_reader,
            args=(process.stderr, self.on_stderr),
            daemon=True
        )

        t1.start()
        t2.start()

    def stream_reader(self, pipe, callback):
        for line in iter(pipe.readline, b''):
            callback(line)
        pipe.close()

    def on_stdout(self, line):
        pass
        # print(line)

    def on_stderr(self, line: bytes):
        line = line.decode(encoding="utf8", errors="ignore").strip()
        pattern = r"^.*https://.*\.trycloudflare\.com.*$"
        link = re.match(pattern, line)
        # print(link)
        # print(f"{link}  ( + )  {line}  LINE ENDS HEAR")
        if link:
            link = link[0].split()[-2]
            show(f"Global Server accessible at: \033[1;33;41m {link} \033[0m")
            show("trying to auto open the link")
            show("=" * os.get_terminal_size()[0])
            time.sleep(3)
            webbrowser.open(link)
            show("still not opend ? please copy the provided link")
            show("=" * os.get_terminal_size()[0])
            

 

