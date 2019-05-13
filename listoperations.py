#!/usr/bin/python

def union(l1,l2):
	l3 = l1
	for x in l2:
		if x not in l3:	
			l3.append(x)
	return l3

def intersection(l1,l2):
	l3=[]
	for x in l1:
		if x in l2:	
			l3.append(x)
	return l3

def spdiff(l1,l2):
	l3=l1
	l4=l2
	for x in l3:
		if x in l4:
			l3.remove(x)
			l4.remove(x)
	l3.extend(l4)
	return l3

def issubset(l1,l2):
	for x in l2:
		if x not in l1:
			return True

def menu():
	ch = -1
	while ch < 1 or ch > 7:
		print("Welcome To List Menu :)")
		print("1.Union\n2.Intersection\n3.Special difference\n4.Check if Subset\n5.Check if Superset\n6.Check if Disjoint\n7.Exit")
		ch = eval(input("Enter Choice"))
	return ch

def operations():
	l1=eval(input("Enter main/first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	ch = menu()
	while(ch != 7):
		if ch == 1:
			print(union(l1,l2))
		elif ch == 2:
			print(intersection(l1,l2))
		elif ch == 3:
			print(spdiff(l1,l2))
		elif ch == 4:
			if issubset(l1,l2):
				print("\nSecond list is not a subset of main list\n")
			else:
				print("\nSecond list is a subset of main list\n")
		elif ch == 5:
			if issubset(l1,l2):
				print("\nMain list is not a superset of second list\n")
			else:
				print("\nMain list is a superset of second list\n")
		elif ch == 6:
			if issubset(l1,l2):
				print("\nMain list is disjoint to second list\n")
			else:
				print("\nMain list is not disjoint to second list\n")
		else:
			break
		ch = menu()


def main():
	operations()


if __name__ == '__main__':
	main()






