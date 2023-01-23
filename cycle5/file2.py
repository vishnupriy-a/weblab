f1=fopn("t.txt","r")
a=[y.rstrip() for x,y in enumerate(f1) if x%2==0]
f1.close()
f2=open("t2.txt","w+")
[f2.write(str(a[i]+"\n")for i in range(len(a))]
f2.seek(0)
print("file 2 content : \n",f2.read()]
f2.close()
