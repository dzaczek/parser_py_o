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
class Parser:
    def __init__(self, filename):
        self.filname=filename
        print self.filname
        self.fcat=self.Mreadfile()
        self.cutter()
    def Mreadfile(self):
        self.file=open(self.filname,"r")
        self.data=self.file.read()
        self.file.close()
        return self.data
    def cutter(self):
        print self.fcat
        #for line in self.fcat:
        
        self.abc=re.search(regex, self.fcat,re.M|re.I)
        print self.abc.group(1),self.abc.group(2)
            #Login:\s+(\S+)\s+Account\s+decription:\s+(.*)\n


class IterParser(FilesName,Parser):
    def __init__(self, patch):
        self.start1=FilesName(patch)
        self.filelist=self.start1.ReturnTuple()
        self.serversc=[]
        self.UserList=[]


    def  iterfillist(self):
         for indexm, patchvar in enumerate(self.filelist):
             print indexm, patchvar
             self.start8=Parser(patchvar)
             self.appendserv(self.nameserver(patchvar))

             #self.UserList.append(UserIndex())

    def appendserv(self,servername):
        self.serversc.append(servername)

    def  printserc(self):
        print self.serversc

    def  displayAUDIT(self):
         self.start1.displayFileList()
         print self.filelist

    def nameserver(self, line):
        return os.path.basename(line[:line.rfind('.')])

class UserIndex:
        def __init__(self, username=None,servername=None,comment=None):
            self.username=username
            self.comment=comment
            self.servername=servername

        def dispalyuser(self):
            print username+" "+comment+" "+servername


#Startapp=FilesName("logs")
#Startapp.displayFileList()
Startapp=IterParser("logs")
Startapp.displayAUDIT()
Startapp.iterfillist()
Startapp.printserc()
