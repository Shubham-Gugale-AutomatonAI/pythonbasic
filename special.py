#!/usr/bin/python

def special():
	x=eval(input("Enter a number: "))
	y=x
	c=0
	while(x>0):
		z=x%10
		a=1
		for b in range(1,z):
			a=a*(b+1)
		c=c+a
		x=x//10
	if(c==y):
		print("The number %d is special" %y)
	else:
		print("The number %d is not special" %y)

special()

