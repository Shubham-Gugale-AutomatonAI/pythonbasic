# To accpet 2 lists from user and find intersection of both

#!/usr/bin/python

def intersection(l1,l2):
	l3=[]
	for x in l1:
		if x in l2:	
			l3.append(x)
	return l3

def main():
	l1=eval(input("Enter first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	result=intersection(l1,l2)
	print(result)

if __name__ == '__main__':
	main()
