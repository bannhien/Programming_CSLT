so_am=0
so_duong=0
while True:
    n=int(input())
    if n<0:
        so_am+=1
    elif n>0:
        so_duong+=1
    else:
        break
print(f"{so_duong} so duong")
print(f"{so_am} so am")