import re
import glob
import os

regex = r"Login:\s+(\S+)\s+Account\s+decription:\s+(.*)\n"

class FilesName:
    filenamelist=[]
    def __init__(self, patch):
        self.filenamelist=glob.glob(patch+"/*.txt")
        #print self.filenamelist
    def  displayFileList(self):
        print self.filenamelist
    def  ReturnTuple(self):
        return self.filenamelist

class UserIndex:
        def __init__(self, username=None,comment=None,servername=None):
            self.username=username
            self.comment=comment
            self.servername=servername

        def displayuser(self):
            print self.username+" "+self.comment+" "+self.servername


class IterParser(FilesName, UserIndex):
    def __init__(self, patch):
        self.start1=FilesName(patch)
        self.filelist=self.start1.ReturnTuple()
        self.serversc=[]
        self.UserList=[]


    def  iterfillist(self):
         for indexm, patchvar in enumerate(self.filelist):
             print indexm, patchvar
             self.workservername=self.nameserver(patchvar)
             self.cutter(self.Mreadfile(patchvar),self.workservername)
             self.appendserv(self.workservername)

             #self.UserList.append(UserIndex())
    def Mreadfile(self,filename):
        self.file=open(filename,"r")
        self.data=self.file.read()
        self.file.close()
        return self.data

    def add_user(self,user,note,servername):
        self.UserList.append(UserIndex(user,note,servername))

    def cutter(self, data,servn):
        self.regex="Login:\s+(\S+)\s+Account\s+decription:\s+(.*)"
        for line in data.splitlines():
            self.abc=re.search(self.regex,line)
            if self.abc:
                self.add_user(self.abc.group(1),self.abc.group(2),servn)
                print self.abc
                #print abc.group()
                print self.abc.group(1), self.abc.group(2),servn


    def appendserv(self,servername):
        self.serversc.append(servername)

    def  printserc(self):
        print self.serversc

    def  displayAUDIT(self):
         self.start1.displayFileList()
         print self.filelist

    def nameserver(self, line):
        return os.path.basename(line[:line.rfind('.')])


#Startapp=FilesName("logs")
#Startapp.displayFileList()
Startapp=IterParser("logs")
Startapp.displayAUDIT()
Startapp.iterfillist()
Startapp.printserc()
