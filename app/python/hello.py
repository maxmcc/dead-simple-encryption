import os
import subprocess
import sys

os.chdir(os.path.expanduser("~/Desktop"))
for arg in sys.argv:
    subprocess.call("echo '" + arg + "' >> arguments.txt", shell=True)
