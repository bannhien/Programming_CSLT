D={}
dem=1
while True:
    nhap=input()
    
    if nhap=="":
        break
    hoten, tuoi=nhap.split()
    D[dem]={"name": hoten, "age": tuoi}
    dem+=1
print(D)