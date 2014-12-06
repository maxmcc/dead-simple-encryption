def splitFile(filename, chunkSize):
	f = open(filename,"rb") #assume binary
	data = f.read()
	f.close()
	fileSize = len(data) #get size of data, don't need to import os

	counter = 0
	for i in range(0, fileSize+1, chunkSize): #add 1 to fileSize to iterate through all bytes, step through each split
		print "Writing {0} chunk!".format(counter) 
		chunkName = "chunk{0}".format(counter)
		
		output = open(chunkName, "wb") #assume binary again, write to a new file
		output.write(data[i:i+chunkSize]) #write from the end of previous to the length of the chunk size
		output.close()
		counter+=1

splitFile("input.jpg",1024*1024*5)
		
	
	

