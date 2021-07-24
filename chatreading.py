import os

def pydrive2install():
    os.system("start cmd /c pip install pydrive2")

pydrive2install()

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

import time

def cls():
    print("\f")
    os.system('cls' if os.name=='nt' else 'clear')
    
def startmessagewrite():
    directory = os.getcwd()
    cmd = 'start cmd /k "cd ' + directory + '\\Downloads & py chatwriting.py"'
    os.system(cmd)

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