#!/usr/bin/python

def reverse():
	x=eval(input("Enter a number: "))
	z=x
	rev=0
	while(x>0):
		y=x%10
		rev=rev*10+y
		x=x//10
	print("Reverse is ",rev)	
	if z==rev:
		print("The number is palindrome")
	else:
		print("The number is not palindrome")
reverse()
