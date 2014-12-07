from zipfile import *
import os
import shutil

def make_zip(*args):
	for file in args:
		with ZipFile("zippedFiles.zip",'w',allowZip64=True) as zip:
			zip.write(file)
	return 1

def unzip(zipfile):
	os.mkdir(zipfile.strip(".zip"))
	moveDir = os.getcwd() + "/" + zipfile.strip(".zip")
	zipped = ZipFile(file=zipfile,allowZip64=True)
	zipped.extractall(moveDir)
	zipped.close()
	os.chdir(moveDir)
	return 1

