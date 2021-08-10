from time import gmtime, strftime
import os
import sys

try:
    from pydrive2.auth import GoogleAuth
    from pydrive2.drive import GoogleDrive
    import climage
    from PIL import UnidentifiedImageError
    from ansimarkup import AnsiMarkup
    from ansimarkup.markup import MismatchedTag
    from ansimarkup.markup import UnbalancedTag
except ModuleNotFoundError:
    print("Please run 'setup.py' first! Also, you're not supposed to run this script anyway!")
    sys.exit()

def cls():
    print("\f")
    os.system('cls' if os.name=='nt' else 'clear')

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.access_token_expired:
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
   replyornot = False
   imgornot = False
   if len(newmessage) > 2 and newmessage[0] and newmessage[-1] == "," and "|" in newmessage:
       pos = newmessage.index("|")
       replymessage = newmessage[1:pos]
       reply = newmessage[pos+1:-1]
       if len(reply) > 2 and reply[0] and reply[-1] == "`":
           if "|" in reply:
               pos = reply.index("|")
               caption = reply[pos+1:-1]
               filepath = reply[1:pos]
           else:
               filepath = reply[1:-1]
           try:
               output = climage.convert(filepath, is_unicode=True, is_truecolor=True, is_256color=False)
               if "|" in reply:
                   reply = output + caption
               else:
                   reply = output
           except (FileNotFoundError, UnidentifiedImageError, PermissionError, OSError):
               pass
       newmessage = "<dim>	|" + replymessage + "</dim>"
       newmessage = newmessage + "\n" + "<dim>	|</dim>" + "\n" + reply
       replyornot = True
   if len(newmessage) > 2 and newmessage[0] and newmessage[-1] == "`":
       if "|" in newmessage:
           pos = newmessage.index("|")
           caption = newmessage[pos+1:-1]
           filepath = newmessage[1:pos]
       else:
           filepath = newmessage[1:-1]
       try:
           output = climage.convert(filepath, is_unicode=True, is_truecolor=True, is_256color=False)
           if "|" in newmessage:
               newmessage = output + caption
           else:
               newmessage = output
           imgornot = True
       except (FileNotFoundError, UnidentifiedImageError, PermissionError, OSError):
           pass
   markup = AnsiMarkup(strict=True)
   try:
       markup.parse(newmessage)
   except (MismatchedTag, UnbalancedTag):
       newmessage = markup.strip(newmessage)
   if replyornot == True or imgornot == True:
       newmessage = userenter + ": \n" + newmessage + "        " + str(strftime("%m-%d-%Y %H:%M:%S", gmtime()) + " GMT")
   else:
       newmessage = userenter + ": " + newmessage + "        " + str(strftime("%m-%d-%Y %H:%M:%S", gmtime()) + " GMT")
   chatlogs = drive.CreateFile({"id": "1H1dmPXahBo1BcKk4djuABDom8q2ys-E4"})
   chatlogs.GetContentFile("chatlogsforwrite.txt")
   modifyfile = open("chatlogsforwrite.txt", "a", encoding = 'utf-8')
   modifyfile.write(newmessage)
   if imgornot == True:
       modifyfile.write("\n\n")
   else:
       modifyfile.write("\n")
   modifyfile.close()
   modifyfile = open("chatlogsforwrite.txt", "r", encoding = 'utf-8')
   logs = modifyfile.read()
   modifyfile.close()
   chatlogs.SetContentString(logs)
   chatlogs.Upload()