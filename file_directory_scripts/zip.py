from zipfile import *

def make_zip(*args):
	for file in args:
		with ZipFile("zippedFiles.zip",'a',allowZip64=True) as zip:
			zip.write(file)
	return 1
		
def unzip(zipfile):
	zipped = ZipFile(file=zipfile,allowZip64=True)
	zipped.extractall()
	return 1

