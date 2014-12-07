import zip
import splitFiles
import flatten
import AES_encryption
import traversal
import os
import shutil
import dummyDir
import sys
from zipfile import *


def encrypt(password, *args):
	currDir = os.getcwd()
	
	for list in args:
		for file in list:
			with ZipFile("zippedFiles.zip",'a',allowZip64=True) as zip:
				print file
				zip.write(file)

	unEncryptedZips = "zippedFiles.zip"
	key = AES_encryption.makeKey(password)
	workDir = dummyDir.dummyDir(traversal.overFunction(os.path.getsize(unEncryptedZips))[0],currDir)
	unEncryptedZipsFullPath = currDir + "/" + unEncryptedZips
	print unEncryptedZipsFullPath
	shutil.move(unEncryptedZipsFullPath, workDir)
	AES_encryption.encryptFile(unEncryptedZips, key)
	print "key: " + key
	splitFiles.split_file(unEncryptedZips)# + '.enc')
	os.remove(unEncryptedZips + '.enc')
	parentDir, dirName = os.path.split(os.getcwd())
	
	zf = ZipFile(dirName + ".zip", "w")
	files = next(os.walk(os.getcwd()))[2]
	files.remove(dirName + ".zip") #don't include archive
	for file in files:
		zf.write(file)
	zf.close()
	zipfile = os.getcwd() + "/" + dirName + ".zip"
	shutil.move(zipfile, parentDir)
	deleteDir = os.getcwd()
	os.chdir(parentDir)
	shutil.rmtree(deleteDir)
	
if "__main__":
	argList = []
	for arg in sys.argv:
		argList.append(arg)
	del argList[0]
	
	encrypt(argList[0], argList[1:])