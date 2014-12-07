import zip
import splitFiles
import flatten
import AES_encryption
import traversal
import os
import shutil
import dummyDir
from zipfile import *


def encrypt(password, *args):
	currDir = os.getcwd()
	
	for file in args:
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
	splitFiles.split_file(unEncryptedZips + '.enc')
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
	
encrypt("password", "test.txt", "test 2.txt")