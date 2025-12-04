import os
import sys
import stat
import platform
import requests
from global_constants import BINARY_PATH


class CloudflaredInstaller:

    def normalize_arch(self, arch):
        arch = arch.lower()
        if arch in ("x86_64", "amd64"):
            return "amd64"
        if arch in ("arm64", "aarch64"):
            return "arm64"
        raise OSError(f"Unsupported architecture: {arch}")

    def get_platform_info(self):
        os_name = sys.platform
        arch = self.normalize_arch(platform.machine())

        if os_name.startswith("linux"):
            suffix = f"linux-{arch}"
            is_windows = False
        elif os_name == "darwin":
            suffix = f"darwin-{arch}"
            is_windows = False
        elif os_name == "win32":
            suffix = "windows-amd64.exe"   # Cloudflare only ships amd64 for Windows
            is_windows = True
        else:
            raise OSError(f"Unsupported operating system: {os_name}")

        return suffix, is_windows

    def ensure_cloudflared_binary_and_set_path_to_global(self):
        suffix, is_windows = self.get_platform_info()

        if is_windows:
            binary_name = suffix
            download_url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/{suffix}"
        else:
            binary_name = f"cloudflared-{suffix}"
            download_url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/{binary_name}"

        binary_path = os.path.join(os.getcwd(), binary_name)

        if not os.path.exists(binary_path):
            print(f"Downloading cloudflared: {binary_name}")

            with requests.get(download_url, stream=True) as r:
                r.raise_for_status()
                with open(binary_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            if not is_windows:
                os.chmod(binary_path, os.stat(binary_path).st_mode | stat.S_IEXEC)

            print(f"Downloaded to {binary_path}")

        # Prepend working dir to PATH
        os.environ["PATH"] = f"{os.getcwd()}{os.pathsep}{os.environ.get('PATH','')}"
        BINARY_PATH[0] = str(binary_path)
        return binary_path
