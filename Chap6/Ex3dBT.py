D = {}
while True:
    nhap = input()
    
    if nhap == "":
        break
    
    item_ten, item_so = nhap.split()
    
    item_so = int(item_so)

    D[item_ten] = item_so

del_items=[k for k,v in D.items() if v<=100]
for k in del_items:
    del D[k]
print(D)
