#To accept file name from user and print all its line using readline
#Print max length and min length line

#!/usr/bin/python

import io
x=input("Enter File name")
fd=io.FileIO(x)
line=fd.readline()
max=min=line
while line != b'':	
	line=fd.readline()
	if line ==  b'':
		break
	if len(line)<len(min):
		min=line
	if len(line)>len(max):
		max=line
print("Max len line is",max)
print("Min len line is",min)
