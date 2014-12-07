import AES_encryption

def decrypt(file_name, password):
	unzip(file_name)
	extractZip()
	key = makeKey(password)
	decrypt("output.zip", key)
	unzip("output.zip")