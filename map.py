def sum(a,b):
	return a+b
a=["mango","orange"]
b=["juice","juice"]
c=list(map(sum,a,b))
print(c)
a=input("enter the elements:")
a=a.split()
a=list(map(int,a))
print(a)
