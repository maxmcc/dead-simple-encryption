import os

def splitFile(filename):
	f = open(filename,"rb") #assume binary
	data = f.read()
	f.close()
	fileSize = len(data) #get size of data, don't need to import os

	counter = 0
	currBit = 0 #save state of bit
	for file in next(os.walk(os.getcwd()))[2]:
		if (filename != file and file != "splitFiles.py"): #skip if we try to inject in the file were splitting into
			workingFileSize = os.path.getsize(file)
			chunkSize = 0.15 * workingFileSize
			workingFile = open(file, "a+b")
			workingFile.write("\n ---INJECTED DATA--- \n")
		
			print "writing to " + file
		
			if chunkSize > (fileSize - currBit): #remaining bits left
				print "last chunk"
				workingFile.write(data[currBit:])
				workingFile.close()
				break;
			else: #have to go to next file
				print "go to next :("
				workingFile.write(data[currBit:currBit+chunkSize])
				workingFile.close()
				currBit+=chunkSize
splitFile("hide.zip")

			
			
			
			
			
		
		 
		
	
	