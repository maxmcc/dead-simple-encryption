import os

def splitFile(filename):
	f = open(filename,"rb") #assume binary
	data = f.read()
	f.close()
	fileSize = len(data) #get size of data, don't need to import os

	counter = 0
	currBit = 0 #save state of bit
	files = next(os.walk(os.getcwd()))[2]
	for i,file in enumerate(files):
		if (filename != file and file != "splitFiles.py"): #skip if we try to inject in the file were splitting into
			workingFileSize = os.path.getsize(file)
			chunkSize = 0.15 * workingFileSize
			workingFile = open(file, "a+b")
			workingFile.write("\n ---INJECTED DATA--- \n")
			reSplit = open("splitTest.zip", "a+b")
			if chunkSize > (fileSize - currBit): #last chunk
				workingFile.write("next = none \n")
				workingFile.write(data[int(currBit):])
				reSplit.write(data[int(currBit):])
				workingFile.close()
				break
			else: #have to go to next file
				if currBit == 0:
					workingFile.write("--- head --- \n")
				workingFile.write("next = " + files[i+1] + "\n")
				workingFile.write(data[int(currBit):int(currBit+chunkSize+1)])
				reSplit.write(data[int(currBit):int(currBit+chunkSize+1)])
				workingFile.close()
				currBit+=chunkSize
splitFile("hide.zip")

			
			
			
			
			
		
		 
		
	
	