l1=[]
text=input("enter your name:")
a=text.split()
l1.append(a)
cnt=0
for i in a:
	b=i.count('a')
	if b>=1:
		cnt=cnt+b
print(cnt,"times 'a' occured in the list")
		
		
		
