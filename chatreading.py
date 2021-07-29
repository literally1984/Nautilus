import time
import os
import platform
import sys

try:
    from pydrive2.auth import GoogleAuth
    from pydrive2.drive import GoogleDrive
except ModuleNotFoundError:
    print("Please run 'setup.py' first!")
    sys.exit()

if platform.system() == "Darwin":
    from applescript import tell

def cls():
    print("\f")
    os.system('cls' if os.name=='nt' else 'clear')

def startmessagewrite():
    if platform.system() == "Windows":
        directory = os.getcwd()
        cmd = 'start cmd /k "cd ' + directory + '\\Downloads & ' + sys.executable + ' chatwriting.py"'
        os.system(cmd)
    elif platform.system() == "Darwin":
        directory = os.getcwd()
        cmd = "cd " + directory + "/Downloads; " + sys.executable + " chatwriting.py"
        tell.app('Terminal', 'do script "' + cmd + '"', background = True) 
    else:
        print("Unfortunately, Nautilus is not supported on Linux and other systems yet. :/")
        sys.exit()

gauth = GoogleAuth()

gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})
    gauth.LocalWebserverAuth("localhost",[8080])
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

startmessagewrite()

filelastmodified = 0
while True:
    chatfileforread = drive.CreateFile({"id": "1ZbCPNwm6WRZE5irnAP27L5lye5nppmTS"})
    if chatfileforread["modifiedDate"] == filelastmodified:
        time.sleep(1)
        continue
    else:
        cls()
    chatfileforread.GetContentFile("chatlogsforread.txt")
    displaychat = open("chatlogsforread.txt", "r")
    print(displaychat.read())
    displaychat.close()
    filelastmodified = chatfileforread["modifiedDate"]