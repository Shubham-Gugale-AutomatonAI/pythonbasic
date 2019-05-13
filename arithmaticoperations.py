#Write a Python module to perform an arithmetic operations
#When a user executes it as independent python script show him the menu and perform the selected operation.
#!/usr/bin/python

def add(x,y):
	return x+y

def substract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

def floordivide(x,y):
	return x//y

def raisedto(x,y):
	return x**y

def menu():
	ch = -1
	while ch < 1 or ch > 7:
		print("Welcome To List Menu :)")
		print("1.Add\n2.Substract\n3.Multiply\n4.Divide\n5.Floor Division\n6.Raised To\n7.Exit")
		ch = eval(input("Enter Choice"))
	return ch

def operations():
	x=eval(input("Enter first number"))
	y=eval(input("Enter second number"))
	ch = menu()
	while(ch != 7):
		if ch == 1:
			print(add(x,y))
		elif ch == 2:
			print(substract(x,y))
		elif ch == 3:
			print(multiply(x,y))
		elif ch == 4:
			print(divide(x,y))
		elif ch == 5:
			print(floordivide(x,y))
		elif ch == 6:
			print(raisedto(x,y))
		else:
			break
		ch = menu()


def main():
	operations()


if __name__ == '__main__':
	main()

