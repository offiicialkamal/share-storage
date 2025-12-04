import platform
import sys
import os
import requests
import subprocess
import signal
import threading

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
            bufsize=1
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

    def on_stderr(self, line):
        pass




# # Main execution logic
# if __name__ == "__main__":
#     # You will need to install 'requests' first: pip install requests
#     try:
#         # 1. Ensure the binary is present/downloaded
#         cf_binary_path = ensure_cloudflared_binary()
        
#         # 2. Run the tunnel using the downloaded binary
#         run_tunnel(cf_binary_path, local_url="http://localhost:8000")

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         sys.exit(1)
