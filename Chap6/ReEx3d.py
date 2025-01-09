D = {}
while True:
    nhap = input()
    
    if nhap == "":
        break
    
    item_ten, item_so = nhap.split()
    
    item_so = int(item_so)
    
    D[item_ten] = item_so
DCopy=D.copy()
for k,v in DCopy.items():
    if v<=100:
        del(D[k])
print(D)