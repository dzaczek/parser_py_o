#!/usr/bin/python
import re
import glob
import os
import xlsxwriter


class FilesName:
    # find all files txt in directory  patch
    filenamelist = []

    def __init__(self, patch):
        self.filenamelist = glob.glob(patch + "/*.txt")
        # print self.filenamelist

    def displayFileList(self):
        print self.filenamelist

    def ReturnTuple(self):
        return self.filenamelist


class UserIndex:
    # user list

    def __init__(self, username=None, comment=None, servername=None):
        self.username = username
        self.comment = comment
        self.servername = servername

    def displayuser(self):
        print self.username + " " + self.comment + " " + self.servername

    def returnusername(self):
        return self.username

    def returncomment(self):
        return self.comment

    def returnservername(self):
        return self.servername

    def returnall(self):
        return [self.username, self.comment, self.servername]


class XLSmode:
    #create clsx file
    def __init__(self, datax="None", filename="test.xlsx"):
        self.datax = datax
        self.filename = filename
        self.create_file()
        self.row=1
        self.col=1
    def create_file(self):
        workbook = xlsxwriter.Workbook(self.filename)
        worksheet = workbook.add_worksheet()
        header_format = workbook.add_format({
            'border': 1,
            'bg_color': '#FFFF66',
            'bold': True,
            'text_wrap': True,
            'valign': 'vcenter',
            'indent': 1,
        })
        text_format=workbook.add_format({
        'border': 1,

        })
    # Write the header cells and some data that will be used in the examples.
        heading1 = 'Server Name'
        heading2 = 'User Name'
        heading3 = 'Additional Information'
        worksheet.set_column('A:B', 20)
        worksheet.set_column('C:C', 50)
        worksheet.write('A1', heading1, header_format)
        worksheet.write('B1', heading2, header_format)
        worksheet.write('C1', heading3, header_format)
        for i ,varxlsx in enumerate(self.datax):
            print i+1, varxlsx
            worksheet.write_row(i+1,0,tuple(varxlsx),text_format)

        workbook.close


class IterParser(FilesName, UserIndex,XLSmode):
    # general class

    def __init__(self, patch):
        self.start1 = FilesName(patch)
        self.filelist = self.start1.ReturnTuple()
        self.serversc = []
        self.UserList = []
        self.iterfillist()
        self.testa=[["aa","aa","aa"],["bb","bb","bb"]]
        #initiate clsass XLSmode
        self.createxls=XLSmode(self.testa,"Name.xlsx")
    def printUserList(self):
        for iuser in self.UserList:
            print "%s \"%s\" %s" % (iuser.servername, iuser.username, iuser.comment)

    # Iterate files by name .....
    def iterfillist(self):
        for indexm, patchvar in enumerate(self.filelist):
            # print indexm, patchvar
            self.workservername = self.nameserver(patchvar)
            self.cutter(self.Mreadfile(patchvar), self.workservername)
            self.appendserv(self.workservername)

            # self.UserList.append(UserIndex())
    # Open file load file to variable and return
    def Mreadfile(self, filename):
        self.file = open(filename, "r")
        self.data = self.file.read()
        self.file.close()
        return self.data

    def add_user(self, user, note, servername):
        # list userlist storage class object adding new UserIndex object
        self.UserList.append(UserIndex(user, note, servername))
        # print "added"

    def cutter(self, data, servn):
        # Parsing data from data vaiable
        self.regex = "Login:\s+(\S+)\s+Account\s+decription:\s+(.*)"
        for line in data.splitlines():
            self.abc = re.search(self.regex, line)
            if self.abc:
                self.add_user(self.abc.group(1), self.abc.group(2), servn)
                # print self.abc
                # print abc.group()
                # print self.abc.group(1), self.abc.group(2), servn

    def appendserv(self, servername):
        # add servername to server list
        self.serversc.append(servername)

    def printserc(self):
        print self.serversc

    def displayAUDIT(self):
        self.start1.displayFileList()
        print self.filelist

    def nameserver(self, line):
        # cut nameserver from patch to file
        return os.path.basename(line[:line.rfind('.')])


# Startapp=FilesName("logs")
# Startapp.displayFileList()
Startapp = IterParser("logs")


#Startapp.printUserList()
