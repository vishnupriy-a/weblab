l1=[]
l2=[]
size=int(input("enter the size of the list"))
for i in range(size):
	num=int(input("enter an  integer number"))
	l1.append(num)
print("numbers are..",l1)
for i in l1:
	if(i%2!=0):
		l2.append(i)	
print(l2)
	
 
