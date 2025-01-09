year=int(input())

if year%400==0:
    isLeapYear=True
elif year%100==0:
    isLeapYear=False
elif year%4==0:
    isLeapYear=True
else:
    isLeapYear=False
    
if isLeapYear==False:
    print("Khong")
else:
    print("Co")