#!/usr/bin/python


def last1(x):
	return x & (x-1)

def main():
	x=eval(input("Enter the number: "))
	result=last1(x)
	print(result)


if __name__ == '__main__':
	main()

