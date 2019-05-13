#!/usr/bin/python

def add(*args):
	sum=0
	print(type(args))
	for x in args:
		sum+=x
	return sum


print(add(10,20))
print(add(10,20,30))
