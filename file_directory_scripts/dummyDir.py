import flatten
import os
import random
import shutil

def dummyDir(path, currDir):
	print path
	hash = random.getrandbits(16)
	workDir = currDir + "\\" + str(hash)
	print workDir
	shutil.copytree(path, workDir)
	os.chdir(workDir) #move to working dir
	print os.getcwd()
	flatten.flatten()
	return os.getcwd()