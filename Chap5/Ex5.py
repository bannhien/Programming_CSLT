n=int(input("n="))
A=[]
for i in range(1,n+1):
    A.append(int(input()))
    
tong=0
for i in range(0,n):
    if i%2!=0:
        tong=tong+A[i]
print("Tong=",tong,sep="")