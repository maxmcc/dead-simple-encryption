import flatten
import os
import random
import shutil
import traversal

def dummyDir(path, currDir):
	hash = random.getrandbits(16)
<<<<<<< HEAD
	workDir = currDir + "/" + str(hash)
=======
	workDir = os.path.join(currDir, str(hash))
>>>>>>> origin/master
	print workDir
	shutil.copytree(path, workDir)
	os.chdir(workDir) #move to working dir
	print os.getcwd()
	flatten.flatten()
	return os.getcwd()