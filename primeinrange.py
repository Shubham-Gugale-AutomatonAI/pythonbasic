#!/usr/bin/python

def prime():
	lb=eval(input("Enter lowerbound: "))
	ub=eval(input("Enter upperbound: "))
	if lb>ub:
		mb=lb
		lb=ub
		ub=mb
	if ub>1:
		for x in range(lb,ub+1):
     			if x>1:
       				for n in range(2,x):
          				if (x%n)==0:
               					break
       				else:
           				print(x)

prime()

	
