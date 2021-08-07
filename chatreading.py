import time
import os
import platform
import sys
import shutil

try:
    from pydrive2.auth import GoogleAuth
    from pydrive2.drive import GoogleDrive
    from ansimarkup import parse
    import emojis
except ModuleNotFoundError:
    print("Please run 'setup.py' first!")
    sys.exit()

if platform.system() == "Darwin":
    try:
        from applescript import tell
    except ModuleNotFoundError:
        print("Please run 'setup.py' first!")
        sys.exit()
    
def cls():
    print("\f")
    os.system('cls' if os.name=='nt' else 'clear')

def startmessagewrite():
    if platform.system() == "Windows":
        pythonrunner = sys.executable + ' chatwriting.py"'
        pythonrunnerwt = 'wt new-tab -p "Command Prompt" -d "%cd%" cmd /k "' + pythonrunner
        if shutil.which("wt.exe") is None:
            os.system('start cmd /k "' + pythonrunner)
        else:
            os.system("start cmd /c " + pythonrunnerwt)
    elif platform.system() == "Darwin":
        currentdir = os.getcwd()
        cmd = "cd " + currentdir + "; " + sys.executable + " chatwriting.py"
        tell.app('Terminal', 'do script "' + cmd + '"', background = True) 
    else:
        print("Unfortunately, Nautilus is not supported on Linux and other systems yet. :/")
        sys.exit()

gauth = GoogleAuth()

gauth.LoadCredentialsFile("mycreds.txt")

if gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

startmessagewrite()

filelastmodified = 0
while True:
    chatfileforread = drive.CreateFile({"id": "1H1dmPXahBo1BcKk4djuABDom8q2ys-E4"})
    if chatfileforread["modifiedDate"] == filelastmodified:
        time.sleep(0.5)
        continue
    else:
        cls()
    displayingchat = chatfileforread.GetContentString(mimetype = "text/plain")
    displayingchat = emojis.encode(displayingchat)
    print(parse(displayingchat))
    filelastmodified = chatfileforread["modifiedDate"]