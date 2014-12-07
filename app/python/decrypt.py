import AES_encryption
import zip
import extractZip
import os
import sys

def decrypt(file_name, password):
	zip.unzip(file_name)
	extractZip.extractZip()
	key = AES_encryption.makeKey(password)
	AES_encryption.decryptFile("output.zip", key)
	os.rename("output", "output.zip")

#decrypt("26086.zip", "hi")

if "__main__":
	argList = []
	for arg in sys.argv:
		argList.append(arg)
	
	
	decrypt(argList[1], argList[2])