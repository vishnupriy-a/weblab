d1={}
n=int(input("enter the size of the dictionary:\n"))
for i in range(n):
	key=input("enter the key:\n")
	value=input("enter the value:\n")
	d1[key]=value
d1s=dict(sorted(d1.items()))
print("ascendingly sorted dictionary is..:\n",d1s)
d1r=dict(reversed(sorted(d1.items())))
print("descendingly sorted dictionary is..:\n",d1r)



