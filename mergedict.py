d1={}
d2={}
d3={}
n=int(input("enter the size of  dictionary1:\n"))
for i in range(n):
	key=input("enter the key:\n")
	value=input("enter the value:\n")
	d1[key]=value
m=int(input("enter the size of dictionary2:\n") )
for i in range(m):
	key=input("enter the key:\n")
	value=input("enter the value:\n")
	d1[key]=value
d3={**d1,**d2}
for k,v in d3.items():
	if k in d1 and k in d2:
		d3[k]=[v,d1[k]]
print(d3)

