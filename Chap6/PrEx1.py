D={}
while True:
    nhap=input()
    
    if nhap=="":
        break
    ten,tien=nhap.split()
    
    tien=int(tien)
    
    D[ten]=tien
    
Input=input()
input_ten,input_tien=Input.split()
input_tien=int(input_tien)

if input_ten in D:
    D[input_ten]+=input_tien
    
print(D)