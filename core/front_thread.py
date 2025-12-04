import os
import time
import threading
from http import server
import socketserver
import webbrowser as wb
from global_constants import LOCAL_PORT


HANDLER = server.SimpleHTTPRequestHandler

class main_thread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Press Ctrl+C to stop the server.")
        print(f"Serving files from directory: {os.getcwd()}")
        print(f"Local Server accessible at: http://localhost:{LOCAL_PORT[0]}")
        with socketserver.TCPServer(("", LOCAL_PORT[0]), HANDLER) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt as K_err:
                print("Thanks for using our tool")
                print("Please don't forget to star us ! bye bye")
                time.sleep(2)
                wb.open("https://github.com/offiicialkamal")
                httpd.server_close()

        