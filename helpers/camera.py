import os
import subprocess

def take_photo(filename):
	cmd = 'raspistill -o ' + filename + ' -t 1000'
	pid = subprocess.call(cmd, shell=True)
