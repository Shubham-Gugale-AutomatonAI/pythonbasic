#Write a program to accept 2 strings from a user and check if the second one is a rotation of the first one.


#!/usr/bin/python

def rotation(l1,l2):
	l3=l1[::-1]
	if(l2==l3):
		return True

def main():
	l1=input("Enter first string: ")
	l2=input("Enter second string: ")
	if rotation(l1,l2):
		print("one string is rotation of another")
	else:
		print("one string is not rotation of another")

if __name__ == '__main__':
	main()

