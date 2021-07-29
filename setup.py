import platform
import subprocess
import sys

def pydrive2install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyDrive2"])

def applescriptinstall():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "applescript"])

if platform.system() == "Windows":
    pydrive2install()
elif platform.system() == "Darwin":
    pydrive2install()
    applescriptinstall()
else:
    print("Unfortunately, Nautilus is not supported on Linux and other systems yet. :/")
    sys.exit()
currentpythoncmd = sys.executable
print("\nNow that all the needed modules are installed, you can now run 'chatreading.py' using the command '" + currentpythoncmd + " chatreading.py'.")