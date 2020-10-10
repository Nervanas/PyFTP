#!/usr/bin/env python
from ftplib import FTP
import sys

if len(sys.argv) != 5:
	print "Usage:" + sys.argv[0] + " HOST PORT USERNAME PASSWORD"
	print "\nExample: " + sys.argv[0] + " 10.11.1.12 21 anonymous anonymous"
	exit()

# Connection details
HOST = sys.argv[1]
PORT = sys.argv[2]
USER = sys.argv[3]
PASS = sys.argv[4]

ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(user=USER, passwd=PASS)

def downloadFile(name):
    filename = name

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    localfile.close()

def downloadAllFiles():
	data = []
	ftp.dir(data.append)

	for line in data:
		f = line[29:].strip().split(" ", 1)[1]
		downloadFile(f)

def listFiles():
	print  "Files in current directory:"
	print ftp.dir()


if __name__ == '__main__':
	listFiles()
	downloadAllFiles()
