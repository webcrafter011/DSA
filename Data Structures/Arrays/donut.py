import subprocess
import os
import sys

def open_brave():
    # Check the operating system
    if sys.platform == "win32":
        # For Windows, use the Brave executable path
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        subprocess.Popen([brave_path])
    elif sys.platform == "darwin":
        # For macOS, Brave is usually in /Applications
        subprocess.Popen(["open", "-a", "Brave Browser"])
    elif sys.platform == "linux":
        # For Linux, just use "brave" if it's in the PATH
        subprocess.Popen(["brave"])

if __name__ == "__main__":
    open_brave()
