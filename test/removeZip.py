import os

def extractZip():
	files = next(os.walk(os.getcwd()))[2]
	found = False
	for file in files: #find first
		f = open(file, "rb")
		lines = f.readlines()
		f.close()
		for i, line in enumerate(lines):
			if "--- head ---" in line:
				zip = open("output.zip", "a+b")
				for zipLine in lines[i+2:]: #don't include --- head --- or the next pointer
					zip.write(zipLine)
				zip.close()
				nextFile = lines[i+1]
				nextFile = nextFile.strip("next = ")
				nextFile = nextFile.strip("\n")
				found = True
				break
		if found:
			break;
	print "extractZip: "+nextFile
	nextFiles(nextFile)
	
def nextFiles(filename):
	print filename
	f = open(filename, "rb")
	lines = f.readlines()
	f.close()
	for i, line in enumerate(lines):
		if "INJECTED DATA" in line:
			print True
			zip=open("output.zip", "a+b")
			for zipLine in lines[i+2:]:
				zip.write(zipLine)
			zip.close()
			if "next = none \n" in lines[i+1]: #more pointers
				print "at the end!"
				break
			else:
				print "another one"
				nextFile = lines[i+1]
				nextFile = nextFile.strip("next = ")
				nextFile = nextFile.strip("\n")
				nextFiles(nextFile)
extractZip()