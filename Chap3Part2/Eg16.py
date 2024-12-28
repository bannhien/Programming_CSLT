n=int(input("n="))
m=int(input("m="))
s=0
i=n
while i<=m:
    if i%3==0:
        s+=i
    i+=1
print(s)