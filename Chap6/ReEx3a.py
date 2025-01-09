D={}
while True:
    nhap=input()
    if nhap=="":
        break
    item_chu,item_so=nhap.split()
    item_so=int(item_so)
    D[item_chu]=item_so
    
print(D)