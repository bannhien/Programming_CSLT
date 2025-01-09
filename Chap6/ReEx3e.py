D = {}
while True:
    nhap = input()
    
    if nhap == "":
        break
    
    item_ten, item_so = nhap.split()
    
    item_so = int(item_so)
    
    D[item_ten] = item_so

item=input()

if item in D:
    D[item]+=100
print(D)