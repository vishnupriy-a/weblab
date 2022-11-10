str1=list(input("Enter the first string").strip())
str2=list(input("Enter the second string").strip())
d=str1[0]
str1[0]=str2[0]
str2[0]=d
print(''.join(str1)," ",''.join(str2))
