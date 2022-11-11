s1=list(input("enter the string:\n"))
temp=s1[0]
s1[0]=s1[len(s1)-1]
s1[len(s1)-1]=temp
print("exchanged string is:\n")
print(''.join(s1))


