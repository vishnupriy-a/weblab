a=int(input("enter the year"))
yr=2022
years=[]
for x in range(2022,a+1):
	if(x%4==0 and x%100!=0) or (x%400==0):
	  years.append(x)
print(years)

	

	
	