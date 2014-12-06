def extractZip(filename):
	f = open(filename, "rb")
	lines = f.readlines()
	f.close()
	for i, line in enumerate(lines):
		if "INJECTED DATA" in line:
			zip=open("output.zip", "a+b")
			for zipLine in lines[i:]:
				zip.write(zipLine)
			zip.close()
			break;