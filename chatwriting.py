from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

import time
from time import gmtime, strftime
import os

def cls():
    print("\f")
    os.system('cls' if os.name=='nt' else 'clear')

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

cls()

userenter = input("Enter your username: ")
cls()

while True:
   newmessage = input("Enter your message: \n")
   cls()
   newmessage = userenter + ": " + newmessage + "        " + str(strftime("%m-%d-%Y %H:%M:%S", gmtime()) + " GMT")
   chatfileforwrite = drive.CreateFile({"id": "1ZbCPNwm6WRZE5irnAP27L5lye5nppmTS"})
   chatfileforwrite.GetContentFile("chatlogsforwrite.txt")
   modifyfile = open("chatlogsforwrite.txt", "a")
   modifyfile.write(newmessage)
   modifyfile.write("\n")
   modifyfile.flush()
   modifyfile.close()
   modifyfile = open("chatlogsforwrite.txt", "r")
   logsfordrive = modifyfile.read()
   modifyfile.close()
   chatfileforwrite.SetContentString(logsfordrive)
   chatfileforwrite.Upload()