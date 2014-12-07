import AES_encryption
import zip
import extractZip

def decrypt(file_name, password):
	zip.unzip(file_name)
	extractZip()
	key = AES_encryption.makeKey(password)
	AES_encryption.decrypt("output.zip", key)
	zip.unzip("output.zip")
	
decrypt("IMG_1618.zip","password")