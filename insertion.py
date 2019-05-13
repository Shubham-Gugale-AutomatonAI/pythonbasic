#!/usr/bin/python

def insertionsort(l):
	print("Insertion Sort\n")
	for i in range (1,len(l)):
		temp=l[i]
		while i>0 and temp<l[i-1]:
			l[i]=l[i-1]			
			i=i-1
			l[i]=temp
		print(l)
	return l

def main():
	l=eval(input("Enter list of numbers"))
	insertionsort(l)

if __name__ == '__main__':
	main()

