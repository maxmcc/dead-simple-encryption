import zip
import splitFiles
import flatten
import AES_encryption

def encrypt(zips=*args, password):
	zip.makeZip(args)
	
	unEncryptedZips = "zippedFiles.zip"
	
	