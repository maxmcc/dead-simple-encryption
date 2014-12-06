import os
import subprocess

input_pic = str(raw_input("What's your input picture: "))
input_zip = str(raw_input("What's your input zip: "))


if os.name == "nt":
	subprocess.call("copy /b " + input_pic + " + " + input_zip + " output.jpg", shell=True)
	