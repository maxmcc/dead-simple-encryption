import flatten
import os
import random
import shutil

def dummyDir(path):
	hash = random.getrandbits(16)
	workDir = os.getcwd() + "\\" + str(hash)
	print workDir
	shutil.copytree(path, workDir)
	os.chdir(workDir) #move to working dir
	flatten.flatten()

dummyDir("D:/Programming/dead-simple-encryption/file_directory_scripts/test")
	
	
