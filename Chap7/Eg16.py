# D = {}
# while True:
#     nhap = input()
    
#     if nhap == "":
#         break
    
#     item_ten, item_so = nhap.split()
    
#     item_so = int(item_so)

#     D[item_ten] = item_so
# print(D)

D = {}
while True:
    nhap = input()
    
    if nhap == "":
        break
    
    L = nhap.split()
    
    L[1]=int(L[1])

    D[L[0]] = L[1]
print(D)