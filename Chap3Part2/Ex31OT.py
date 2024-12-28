n=int(input("n="))
s=1
for i in range (1,n+1,1):
    s*=i
print(f"{n}!={s}")