import os

def split_file(filename):
    f = open(filename, "rb")  # assume binary
    data = f.read()
    f.close()
    file_size = len(data)  # get size of data, don't need to import os

    curr_bit = 0  # save state of bit
    files = next(os.walk(os.getcwd()))[2]
    for i, f in enumerate(files):
        if filename != f and f != "splitFiles.py":
            # skip if we try to inject in the file were splitting into
			working_file_size = os.path.getsize(f)
			chunk_size = int(0.15 * working_file_size)
			working_file = open(f, "a+b")
			working_file.write("\n ---INJECTED DATA--- \n")
			if curr_bit == 0:
				working_file.write("--- head --- \n")
				print "first file: " + f
            #re_split = open("splitTest.zip", "a+b")
			if chunk_size >= (file_size - curr_bit):  # last chunk
				print "last file: " + f
				working_file.write("next = none \n")
				working_file.write(data[curr_bit:])
				# re_split.write(data[curr_bit:])
				working_file.close()
				break
			else:  # have to go to next file
				working_file.write("next = " + files[i + 1] + "\n")
				working_file.write(data[curr_bit:curr_bit + chunk_size + 1])
				#re_split.write(data[curr_bit:curr_bit + chunk_size + 1])
				working_file.close()
				curr_bit += chunk_size