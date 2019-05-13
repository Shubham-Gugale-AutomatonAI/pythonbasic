#Write a program to add two numbers without using arithematic operators
#To accept 2 numbers from user accept bit position and number of bits to swap of each other
#To accept a list from user and find second max out of it

#!/usr/bin/python


def maxi(x):
	max1=x[0]
	max2=x[1]
	for i in range (len(x)):
		if(x[i]>max1):
			max2=max1	
			max1=x[i]
		elif(x[i]>max2):
			max2=x[i]	
	return max1,max2

def main():
	x=eval(input("Enter list of numbers"))
	result=maxi(x)
	print(result)

if __name__ == '__main__':
	main()

#To implement a stack using list
