def varargs(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(type(args))
	for x in args:
		print(x)
	print(type(kwargs))
	for x in kwargs:
		print(x,kwargs[x])

if __name__=='__main__':
	varargs(10,20,30,40,Name="shubham",Hobby="Playing chess")
	
