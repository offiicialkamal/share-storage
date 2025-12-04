from global_constants import BINARY_PATH
import requests
import platform
import sys
import os

class cloudeflared_installer():
    def __init__(self):
        pass

    def ensure_cloudflared_binary_and_set_path_to_global(self):
        """Downloads the cloudflared binary if it doesn't exist."""
        binary_suffix, is_windows = self.get_platform_info()
        binary_name = f"cloudflared-{binary_suffix}" if not is_windows else "cloudflared.exe"
        binary_path = os.path.join(os.getcwd(), binary_name) # Save to current directory

        if not os.path.exists(binary_path):
            print(f"Downloading required cloudflared binary for your system...")
            download_url = f"github.com{binary_suffix}"
            
            # Windows uses a slightly different URL format without the hyphen if using the .exe extension
            if is_windows:
                download_url = f"github.comwindows-amd64.exe"

            r = requests.get(download_url, allow_redirects=True)
            r.raise_for_status()
            with open(binary_path, 'wb') as f:
                f.write(r.content)
            print(f"Download complete: {binary_path}")

            # Make the file executable on Linux/macOS
            if not is_windows:
                os.chmod(binary_path, 0o755)

        return BINARY_PATH.insert(0,binary_path)
    
    
    def get_platform_info(self):
        """Determine the correct Cloudflare binary name for the current OS/Arch."""
        os_name = sys.platform
        arch = platform.machine().lower()

        if os_name.startswith('linux'):
            suffix = f"linux-{arch}"
        elif os_name == 'darwin': # macOS
            suffix = f"darwin-{arch}"
        elif os_name == 'win32': # Windows
            suffix = f"windows-{arch}.exe"
        else:
            raise OSError(f"Unsupported operating system: {os_name}")

        return suffix, os_name == 'win32'