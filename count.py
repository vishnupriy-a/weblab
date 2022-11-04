text=input("enter a text:")
a=text.split()
i=0
for i in a:
	count=0
	for word in a:
		if i==word:
			count=count+1
	print(i,"present",count,"times")

