# To accpet 2 lists from user and find union of both

#!/usr/bin/python

def union(l1,l2):
	l3 = l1
	for x in l2:
		if x not in l3:	
			l3.append(x)
	return l3

def main():
	l1=eval(input("Enter first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	result=union(l1,l2)
	print(result)

if __name__ == '__main__':
	main()
