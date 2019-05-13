#To implement a stack using list

#!/usr/bin/python

def push(l1,data):
	l1.append(data)
	
def pop(l1):
	return l1.pop()


def peep(l1):
	return l1[-1]


def isfull(l1):
	return len(l1) == 10

def isempty(l1):
	return l1 == []
		
def menu():
	ch = -1
	while ch < 1 or ch > 4:
		print("Welcome To Stack Menu !!!")
		print("1.push\n2.pop\n3.peep\n4.exit")
		ch = eval(input("Enter Choice"))
	return ch

def stackoperations():
	l = []
	ch = menu()
	while(ch != 4):
		if ch == 1:
			if not isfull(l):
				push(l, eval(input("Enter data to push:")))
			else:
                		print("Please pop something first, stack is full.")
		elif ch == 2:
			if not isempty(l):
				print(pop(l))
			else:
				print("Stack is empty.")
		elif ch == 3:
			if not isempty(l):
				print(peep(l))
			else:
				print("Stack is empty.")
		else:
			break
		ch = menu()

def main():
	stackoperations()
	
if __name__ == "__main__":
	main()



       
