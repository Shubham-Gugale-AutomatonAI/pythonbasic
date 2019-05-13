#!/usr/bin/python

def add(a,b):
	return a+b
x=0
y=1
while(y!=0):
	y=eval(input("Enter next number or enter 0 to stop:"))
	x=add(x,y) 
print(x)
