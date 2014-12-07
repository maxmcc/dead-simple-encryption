import os

def extractZip():
	files = next(os.walk(os.getcwd()))[2]
	found = False
	hasNextFile = True
	for file in files: #find first
		print file
		f = open(file, "rb")
		lines = f.readlines()
		f.close()
		for i, line in enumerate(lines):
			if "--- head ---" in line:				
				zip = open("output.zip", "a+b")
				for zipLine in lines[i+2:]: #don't include --- head --- or the next pointer
					zip.write(zipLine)
				zip.close()
				print i
				nextFile = lines[i+1]
				if "next = none" in nextFile:
					hasNextFile = False
				nextFile = nextFile.strip("next = ")
				nextFile = nextFile.strip("\n")
				found = True
				break
		if found:
			break
	print "extractZip: "+nextFile
	if hasNextFile:
		nextFiles(nextFile)
	
def nextFiles(filename):
	print filename
	f = open(filename, "rb")
	lines = f.readlines()
	f.close()
	for i, line in enumerate(lines):
		if "next = " in line:
			print True
			zip=open("output.zip", "a+b")
			for zipLine in lines[i+1:]:
				zip.write(zipLine)
			zip.close()
			if "next = none \n" in lines[i]: #none
				print "at the end!"
				break
			else:
				print "another one"
				nextFile = lines[i]
				nextFile = nextFile.strip("next = ")
				nextFile = nextFile.strip("\n")
				nextFiles(nextFile)