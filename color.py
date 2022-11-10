color=list(input("enter the colors:\n").split(" "))
temp=color[0]
color[0]=color[len(color)-1]
color[len(color)-1]=temp
print(color)
	