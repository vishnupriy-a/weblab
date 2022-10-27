l1=[]
l2=[]
n=int(input("enter the size of the first list"))
m=int(input("enter the size of the second list"))
print("enter the elements of a")
for i in range(1,n+1):
	a=int(input())
	l1.append(a)
print("enter the elements of b")
for i in range(1,m+1):
	b=int(input())
	l2.append(b)
print(l1)
print(l2)
print("check whether the two lists are of same length:\n")
if(n==m):
	print(" lists are of same length")
else:
	print("lists are of different length\n")
print("check whether two lists are o same sum")
s1=sum(l1)
s2=sum(l2)
if(s1==s2):
	print("the sum of two lists are same\n")
else:
	print("the sum of two lists are different\n")
print("check whether  any value occur in both lists\n")
c=[]
for x in l1:
	for y in l2:
		if(x==y):
			c.append(x)
if(len(c)>0):
	print(c)
else:
	print("no elements occur")



  	