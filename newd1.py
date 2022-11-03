d1={}
d2={}
#D3={**d1,**d2}
n=int(input("enter the no of items"))
for i in range(n):
	key=input("enter the keyvalue:")
	value=input("enter the valu:")
	d1[key]=value
print(f"d1 =>{d1}")
n=int(input("enter the no of items"))
for i in range(n):
	key=input("enter the keyvalue:")
	value=input("enter the valuE:")
	d2[key]=value
print(f"d2 =>{d2}")
#print("after merging d1 with d2")
#d1.update(d2)
#print(d1)
D3={**d1,**d2}
for k,v in D3.items():
	if k in d1 and k in d2:
		D3[k]=[v,d1[k]]
print(D3)
