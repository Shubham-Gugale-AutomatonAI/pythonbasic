#To accept file name from user and print all its line using readline

#!/usr/bin/python

import io
x=input("Enter File name")
fd=io.FileIO(x)

line=fd.readline()
while line != b'':
	print(line)
	line=fd.readline()
