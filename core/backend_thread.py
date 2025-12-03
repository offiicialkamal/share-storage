
import platform
import sys
import os
import requests
import subprocess
import signal

class secondary_thread:
    def __init__():
        pass

    def start(self):
        pass







def get_platform_info():
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

def ensure_cloudflared_binary():
    """Downloads the cloudflared binary if it doesn't exist."""
    binary_suffix, is_windows = get_platform_info()
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

    return binary_path

def run_tunnel(binary_path, local_url="http://localhost:8000"):
    """Starts the anonymous tunnel process."""
    print(f"Starting tunnel for {local_url} using: {binary_path}")
    
    # Use subprocess to run the binary
    command = [binary_path, "tunnel", "--url", local_url, "--no-autoupdate"]
    
    # Simple run demonstration (use the previous script for URL capture/graceful exit)
    process = subprocess.Popen(command)

    # Keep the script running until interrupted
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\nTerminating tunnel process...")
        process.terminate()
        process.wait()

# Main execution logic
if __name__ == "__main__":
    # You will need to install 'requests' first: pip install requests
    try:
        # 1. Ensure the binary is present/downloaded
        cf_binary_path = ensure_cloudflared_binary()
        
        # 2. Run the tunnel using the downloaded binary
        run_tunnel(cf_binary_path, local_url="http://localhost:8000")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
