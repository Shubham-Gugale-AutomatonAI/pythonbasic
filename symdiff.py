# To accpet 2 lists from user and find symmetric difference of both

#!/usr/bin/python

def intersection(l1,l2):
	l3=[]
	for x in l1:
		if x in l2:	
			l3.append(x)
	return l3

def union(l1,l2):
	l3 = l1
	for x in l2:
		if x not in l3:	
			l3.append(x)
	return l3

def symdiff(l4,l3):
	l5=l4-l3
	return l5

def main():
	l1=eval(input("Enter first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	l3=intersection(l1,l2)
	print("Intersection",l3)
	l4=union(l1,l2)
	print("Union",l4)
	l5=symdiff(l4,l3)
	print("Union",l5)

if __name__ == '__main__':
	main()

