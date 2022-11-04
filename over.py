l1=[]
l2=[]
value=int(input("enter the size of the list"))
for i in range(value):
	num=int(input("enter the number:"))
	if(num>100):
		l2.append("over")
	else:
		l2.append(num)
print(l2)
	
