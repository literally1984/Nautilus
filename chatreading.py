import time
import os
import platform
import sys

try:
    from pydrive2.auth import GoogleAuth
    from pydrive2.drive import GoogleDrive
    import emojis
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
        cmd = 'start cmd /k "' + sys.executable + ' chatwriting.py"'
        os.system(cmd)
    elif platform.system() == "Darwin":
        currentdir = os.getcwd()
        cmd = "cd " + currentdir + "; " + sys.executable + " chatwriting.py"
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
    chatfileforread = drive.CreateFile({"id": "1ksTiAwp1a5rgKfSEv54l7nZM0vD5U46A"})
    if chatfileforread["modifiedDate"] == filelastmodified:
        time.sleep(1)
        continue
    else:
        cls()
    chatfileforread.GetContentFile("chatlogsforread.txt")
    displaychat = open("chatlogsforread.txt", "r")
    displayingchat = displaychat.read()
    print(emojis.encode(displayingchat))
    displaychat.close()
    filelastmodified = chatfileforread["modifiedDate"]