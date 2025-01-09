D={}
while True:
    nhap=input()
    
    if nhap=="":
        break
    ten,diem=nhap.split()
    
    diem=float(diem)
    
    D[ten]=diem
    
for k,v in D.items():
    if v>=4.0:
        print(k)