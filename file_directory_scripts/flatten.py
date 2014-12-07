import os
import shutil

def flatten():
	rootDir = os.getcwd()
	rootSubDirs = next(os.walk(rootDir))[1] #number of dirs
	
	while len(rootSubDirs) != 0:
		dirs = next(os.walk(os.getcwd()))[1] #creates list of directories

		while len(dirs) != 0: #depth search
			os.chdir(dirs[0])
			dirs = next(os.walk(os.getcwd()))[1]
			
		files = next(os.walk(os.getcwd()))[2]
		print "working in " + os.getcwd()
		#move all files in that directory
		for file in files:
			parentDirectory = os.path.dirname(os.getcwd())
			fileToMove = os.getcwd() + "/" + file

			shutil.move(fileToMove, parentDirectory)
			print "moved " + fileToMove + " to " + parentDirectory

		removeDir = os.getcwd()
		parentDirectory = os.path.dirname(os.getcwd())
		os.chdir(parentDirectory)
		shutil.rmtree(removeDir)
		
		rootSubDirs = next(os.walk(rootDir))[1]

flatten()