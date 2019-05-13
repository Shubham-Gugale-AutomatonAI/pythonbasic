#!/usr/bin/python
#To accept a number from user, accept bit position and number of bits to turn off from the given position)

def turnoffbits(x,pos,numofbits)
	x=eval(input("Enter the number: ")
	pos=eval(input("Enter bit position to be turned off: ")
	numofbits=eval(input("number of bits to be turned off: ")
	a=(2**numofbits)-1
	b=a << pos
	c=~b
	d=x&c
	print(d)

	
