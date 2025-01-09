D={}
while True:
    nhap=input()
    
    if nhap=="":
        break
    ten,mon=nhap.split()
    
    D[ten]=mon
    
nhap_mon=input()

for k,v in D.items():
    if v==nhap_mon:
        print(k)