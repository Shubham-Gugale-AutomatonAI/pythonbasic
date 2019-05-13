# To accpet 2 lists from user and find union of both

#!/usr/bin/python

def union(l1,l2):
	l3 = []	
	for i in range (len(l1)):
		for j in range (len(l2)):
			if l1[i]==l2[j]:
				l2.pop(l2[j])
		
	l3.extend(l1[i:])
	l3.extend(l2[j:])


def main():
	l1=eval(input("Enter first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	l3=union(l1,l2)
	print(l3)	
	
if __name__ == '__main__':
	main()
