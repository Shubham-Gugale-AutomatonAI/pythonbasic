#!/usr/bin/python


def pattern1():
	x=eval(input("Number of lines to be printed: "))
	for i in range(x):
		for j in range(i+1):
			print("* ",end="")
		print("\r")

pattern1()

def pattern2():
	y=eval(input("Number of lines to be printed: "))
	a=y
	for i in range(y):
		for j in range(a): 
            		print(end=" ")
		a=a-1
		for j in range(i+1):
			print("* ",end="")
		print("\r")

pattern2()

def pattern3():
	z=eval(input("Number of lines to be printed: "))
	b=2*z-1
	for i in range(z):
		for j in range(b): 
            		print(end=" ")
		b=b-2
		for j in range(i+1):
			print("* ",end="")
		print("\r")

pattern3()
