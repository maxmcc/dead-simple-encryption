<<<<<<< HEAD
import os
import subprocess
import random
=======
"""import os
import subprocess
import random """
>>>>>>> bf5ac1f2699aaa6c5ef9abdce710a47960dfb686
from zipfile import *



def make_zip(*args):
	for file in args:
		with ZipFile("zippedFiles.zip",'a',allowZip64=True) as zip:
			zip.write(file)
	return 1
		
make_zip("text 1.txt", "text 2.txt")
		
def unzip(zipfile):
	zipped = ZipFile(file=zipfile,allowZip64=True)
	zipped.extractall()
	return 1
	
"""def compress_to_image(input_pic, input_zip):
    random_hash = str(random.getrandbits(16))
    with ZipFile(file="backup" + random_hash + ".zip",
                 mode="a",
                 compression=ZIP_DEFLATED,
                 allowZip64=True) as output_zip:
        output_pic = "output_picture.jpg"
        subprocess.call("cat " + input_pic + " " + input_zip + " > "
                        + output_pic, shell=True)
        # FIXME need Win implementation
        output_zip.write(filename=output_pic)
        output_zip.close()
        os.remove(output_pic)


def decompress_from_images(input_pics):
    input_zip = ZipFile(file=input_pics, mode="r")
    injected_files = input_zip.namelist()
    for f in injected_files:
        f.extractall()
"""

# compress_to_image("unsuspect_picture.jpg", "secret_payload1.zip")
# decompress_from_image()

