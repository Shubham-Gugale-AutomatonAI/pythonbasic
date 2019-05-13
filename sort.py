#!/usr/bin/python

def bubblesort(l):
	print("Bubble Sort\n")
	for i in range (len(l)):
		for j in range (len(l)-i-1):
			if l[j]>l[j+1]:				
				temp=l[j] 
				l[j]=l[j+1]
				l[j+1]=temp
		print(l)
	return l

def selectionsort(l):
	print("Selection Sort\n")
	for i in range (len(l)-1):
		small=l[i]
		for j in range (i+1,len(l)):
			if small>l[j]:
				temp=small				
				small=l[j]
				l[j]=temp
		l[i]=small
		print(l)
	return l

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
	bubblesort(l)
	selectionsort(l)
	insertionsort(l)

if __name__ == '__main__':
	main()


