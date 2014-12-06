import os
import subprocess


def compress_to_image():
    input_pic = str(raw_input("What's your input picture: "))
    input_zip = str(raw_input("What's your input zip: "))

    if os.name == "nt":
        subprocess.call("copy /b " + input_pic + " + " + input_zip + " output.jpg", shell=True)
    elif os.name == "posix":
        subprocess.call("cat " + input_pic + " " + input_zip + " > output.jpg", shell=True)


def decompress_from_image():
    input_pic = str(raw_input("What's your input picture: "))

    if os.name == "nt":
        pass
    elif os.name == "posix":
        subprocess.call("unzip " + input_pic, shell=True)