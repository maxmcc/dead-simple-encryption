import AES_encryption
import zip
import extractZip
import os

def decrypt(file_name, password):
	zip.unzip(file_name)
	extractZip.extractZip()
	key = AES_encryption.makeKey(password)
	AES_encryption.decryptFile("output.zip", key)
	os.rename("output", "output.zip")

decrypt("50850.zip", "password")