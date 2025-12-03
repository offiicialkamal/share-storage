import os
from http import server
import socketserver
import webbrowser as wb


PORT = 3356


HANDLER = server.SimpleHTTPRequestHandler

class main_thread:
    def __init__(self):
        pass

    def start(self):
        print(f"Serving files from directory: {os.getcwd()}")
        print(f"Server accessible at: http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt as K_err:
                print("Thanks for using our tool")
                print("Please don't forget to star us ! bye bye")
                wb.open("https://github.com/offiicialkamal")
                httpd.server_close()

        