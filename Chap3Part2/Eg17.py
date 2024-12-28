n=int(input("n="))
m=int(input("m="))
s=0
for i in range (n,m+1,1):
    if i%3==0:
        s+=i
print(s)