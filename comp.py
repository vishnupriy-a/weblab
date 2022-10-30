a=[3.6,-8.9,-6,-3,66]
b=[x for x in a if x>0]
print(b)
c=[x*x for x in a ]
print(c)
y=input("enter a word:\n")
m=['a', 'e','i','o','u','A','E','I','O','U']
p=[x for x in y if x in m]
print(p)
d=[ord(i) for i in y]
print(d)