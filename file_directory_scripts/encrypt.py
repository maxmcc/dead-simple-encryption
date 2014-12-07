import zip
import splitFiles
import flatten
import AES_encryption
import traversal
import os
import shutil


def encrypt(zips=*args, password):
	zip.makeZip(args)
	
	unEncryptedZips = "zippedFiles.zip"
	key = AES_encyrption.makeKey(password)
	workDir = dummyDir(traversal.overFunction(os.path.getsize(unEncryptedZips))[0])
	unEncryptedZipsFullPath = os.getcwd() + "/" + unEncryptedZips
	shutil.move(unEncryptedZipsFullPath, workDir)
	chdir(workDir)
	encrypt(unEncryptedZips, key)
	splitFiles(unEncryptedZips + '.enc')

	
	