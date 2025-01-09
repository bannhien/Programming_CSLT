D = {}
while True:
    nhap = input()
    
    if nhap == "":
        break
    
    item_ten, item_so = nhap.split()
    
    item_so = int(item_so)

    D[item_ten] = item_so
found = False
for k,v in D.items():
    if v >= 200:
        if found:
            print(", ", end="")
        print(k, end="")
        found = True

