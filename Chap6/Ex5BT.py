lop_hoc={}
index=1
while True:
    nhap=input()
    
    if nhap=="":
        break
    hoten, tuoi=nhap.split()
    tuoi=int(tuoi)
    lop_hoc[index]={"name":hoten,"age":tuoi}
    index+=1
    
print(lop_hoc)