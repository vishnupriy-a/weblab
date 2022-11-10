str=list(input("enter a string:\n").lower())
b=str[0]
x=b+""
print("changed string is..\n")
for i in range(1,len(str)):
    if(str[i]==b):
        str[i]='$'
    x+=str[i]
print(x)