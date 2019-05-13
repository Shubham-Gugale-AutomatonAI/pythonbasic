#!/usr/bin/python

def sort(l):
	for i in range (len(l)):
		for j in range (i+1,len(l)):
			if l[i]>l[j]:				
				temp=l[j] 
				l[j]=l[i]
				l[i]=temp
	return l

def merge(l1,l2):
	i=0
	j=0
	l3 = []
	while (i<len(l1) and j<len(l2)):
		if l1[i]<l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i<len(l1):
		l3.extend(l1[i:])
	if j<len(l2):
		l3.extend(l2[j:])
	return l3

def main():
	l1=eval(input("Enter first list of numbers"))
	l2=eval(input("Enter second list of numbers"))
	l1=sort(l1)
	print(l1)
	l2=sort(l2)
	print(l2)
	l3=merge(l1,l2)
	print(l3)


if __name__ == '__main__':
	main()
