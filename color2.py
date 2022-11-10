l1=list(input("enter colors in l1:\n").split())
l2=list(input("enter colors in l2:\n").split())
l3=[]
for i in l1:
	if i not in l2:
		l3.append(i)
print(l3)
