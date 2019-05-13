#!/usr/bin/python
#To accept a number from user, accept bit position and number of bits to turn off from the given position)

def turnoffbits(no,pos,noofbits):
	x = 2**noofbits - 1
	x = x << (pos - noofbits)
	x = ~x
	return no & x
	
def turnOnBits(no,pos,noofbits):
	x = 2**noofbits - 1
	x = x << (pos - noofbits)
	return no | x
	
def toggleOnBits(no,pos,noofbits):
	x = 2**noofbits - 1
	x = x << (pos - noofbits)
	return no ^ x

def rightmosttoggle(no)
	

def main():
	no=eval(input("Enter the number: "))
	pos=eval(input("Enter bit position to be turned off: "))
	noofbits=eval(input("number of bits to be turned off: "))
	result=turnoffbits(no,pos,noofbits)
	print(result)
	result=turnOnBits(no,pos,noofbits)
	print(result)
	result=toggleOnBits(no,pos,noofbits)
	print(result)

if __name__ == '__main__':
	main()



#Write a program to add two numbers without using arithematic operators
#To accept 2 numbers from user accept bit position and number of bits to swap of each other


