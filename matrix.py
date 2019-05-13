#Write a menu driven program to support the following matrix operations:

#!/usr/bin/python

def add(x,y):
	for i in range(len(x)):
		for j in range(len(x[0])):
			r[i][j]=x[i][j]+y[i][j]
	return r

def substract(x,y):
	for i in range(len(x)):
		for j in range(len(x[0])):
			r[i][j]=x[i][j]-y[i][j]
	return r

def multiply(x,y):
	for i in range(len(x)):
		for j in range(len(x[0])):
			r[i][j]=x[i][j]*y[i][j]
	return r

def menu():
	ch = -1
	while ch < 1 or ch > 5:
		print("Welcome To List Menu :)")
		print("1.Add\n2.Substract\n3.Multiply\n4.Display\n5.Exit")
		ch = eval(input("Enter Choice"))
	return ch

def operations():
	x=eval(input("Enter first matrix"))
	y=eval(input("Enter second matrix"))
	ch = menu()
	while(ch != 5):
		if ch == 1:
			add(x,y):
				for n in result:
					print(n)
		elif ch == 2:
			substract(x,y):
				for n in result:
					print(n)
		elif ch == 3:
			multiply(x,y):
				for n in result:
					print(n)
		elif ch == 4:
			print("x=")
			for n in x:
				print(n)
			print("y=")
			for n in y:
				print(n)
		else:
			break
		ch = menu()

def main():
	operations()

if __name__ == '__main__':
	main()
