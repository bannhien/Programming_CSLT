S=0
n=int(input("Nhap n="))

for i in range(1,n+1):
    print(f"So thu {i}:",end="")
    x=int(input())
    
    if x<0:
        continue
    elif x==0:
        break
    else:
        S+=x
print(f"S={S}")