#!/usr/bin/python


# ██████   █████  ██████  ███████ ███████ ██████
# ██   ██ ██   ██ ██   ██ ██      ██      ██   ██
# ██████  ███████ ██████  ███████ █████   ██████
# ██      ██   ██ ██   ██      ██ ██      ██   ██
# ██      ██   ██ ██   ██ ███████ ███████ ██   ██



import re
import glob
import os
import xlsxwriter
import sys
import argparse
import datetime
import string
__author__ = 'SmFjZWsgWmFsZXNraQo='


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


        # ██    ██ ███████ ███████ ██████  ███████
        # ██    ██ ██      ██      ██   ██ ██
        # ██    ██ ███████ █████   ██████  ███████
        # ██    ██      ██ ██      ██   ██      ██
        #  ██████  ███████ ███████ ██   ██ ███████



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

        # ██   ██ ██      ███████ ██   ██
        #  ██ ██  ██      ██       ██ ██
        #   ███   ██      ███████   ███
        #  ██ ██  ██           ██  ██ ██
        # ██   ██ ███████ ███████ ██   ██


class XLSmode:
    # create clsx file

    def __init__(self, datax="None", filename=str(datetime.datetime.now()) + ".xlsx"):
        self.datax = datax
        self.filename = filename
        self.create_file()
        self.row = 1
        self.col = 1

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
        text_format = workbook.add_format({
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
        worksheet.autofilter('A1:D11')
        worksheet.freeze_panes(1, 0)
        worksheet.autofilter(0, 0, len(self.datax) + 1, 2)
        for i, varxlsx in enumerate(self.datax):
            # print i + 1, varxlsx
            worksheet.write_row(i + 1, 0, tuple(varxlsx), text_format)

        workbook.close

        # ██ ████████ ███████ ██████
        # ██    ██    ██      ██   ██
        # ██    ██    █████   ██████
        # ██    ██    ██      ██   ██
        # ██    ██    ███████ ██   ██


class IterParser(FilesName, UserIndex, XLSmode):
    # general class

    def __init__(self, patch, foutp):
        self.start1 = FilesName(patch)
        self.filelist = self.start1.ReturnTuple()
        self.serversc = []
        self.UserList = []
        self.iterfillist()
        self.foutp = foutp
        # print len(self.foutp)
        # self.testa=[["aa","aa","aa"],["bb","bb","bb"]]
        # self.foutp=str(datetime.datetime.now())+".xlsx" if len(self.foutp)==0 else print self.foutp
        # print len(self.foutp)
        # initiate clsass XLSmode in paramter list of list [[],[],[]] logs and
        # pach to file
        try:
            len(self.foutp)
        except:
            self.foutp = str(datetime.datetime.now()) + ".xlsx"

        self.createxls = XLSmode(self.listoflist(), self.foutp)

    def printUserList(self):
        for iuser in self.UserList:
            print "%s \"%s\" %s" % (iuser.servername, iuser.username, iuser.comment)

    def listoflist(self):
            # convert UserList data to tuple of tuple
        self.listlist = []
        for iuser in self.UserList:
            self.listlist.append(
                [iuser.servername, iuser.username, iuser.comment])
        return self.listlist

        # ███████ ██ ██      ███████ ███████      ██████  ██████  ██████  ███████ ███    ██
        # ██      ██ ██      ██      ██          ██    ██ ██   ██ ██   ██ ██      ████   ██
        # █████   ██ ██      █████   ███████     ██    ██ ██████  ██████  █████   ██ ██  ██
        # ██      ██ ██      ██           ██     ██    ██ ██      ██      ██      ██  ██ ██
        # ██      ██ ███████ ███████ ███████      ██████  ██      ██      ███████ ██   ████

    def iterfillist(self):
            # Iterate files by name and
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

        #  █████  ██████   ██████  ██████   █████  ██████  ███████ ███████
        # ██   ██ ██   ██ ██       ██   ██ ██   ██ ██   ██ ██      ██
        # ███████ ██████  ██   ███ ██████  ███████ ██████  ███████ █████
        # ██   ██ ██   ██ ██    ██ ██      ██   ██ ██   ██      ██ ██
        # ██   ██ ██   ██  ██████  ██      ██   ██ ██   ██ ███████ ███████


class Startapp(IterParser):

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Simple scipt for conver  logs from many servers to one XLSX file . Script work only witch perl output from another(pp_parser_batch) script  ')
        self.parser.add_argument(
            '-l', '--logs', help='Input the path to log files direcotry', required=True)
        self.parser.add_argument(
            '-o', '--output', help='Input outputfilename', required=False)
        self.args = self.parser.parse_args()
        self.startpraser = IterParser(self.args.logs, self.args.output)
# Startapp=FilesName("logs")
# Startapp.displayFileList() v


# ███████ ████████  █████  ██████  ████████      █████  ██████  ██████
# ██         ██    ██   ██ ██   ██    ██        ██   ██ ██   ██ ██   ██
# ███████    ██    ███████ ██████     ██        ███████ ██████  ██████
#      ██    ██    ██   ██ ██   ██    ██        ██   ██ ██      ██
# ███████    ██    ██   ██ ██   ██    ██        ██   ██ ██      ██


Startapp = Startapp()


#Startapp = IterParser("logs")


# Startapp.printUserList()
