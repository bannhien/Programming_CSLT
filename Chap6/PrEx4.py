n=int(input())
D={}
for i in range(n):
    nhap=input()
    item_ten, item_so = nhap.split()
    
    item_so = int(item_so)
    
    D[item_ten] = item_so
    
sorted_D=sorted(D.items(),
key=lambda item: item[1],
reverse=True)

top_hai=sorted_D[:2]
print(top_hai)