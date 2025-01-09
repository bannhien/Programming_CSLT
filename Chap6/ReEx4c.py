n=int(input())
S=[]
M=[]
for i in range (n):
    chuoi=input()
    S.append(chuoi)
for i in range (n):
    so_nguyen=int(input())
    M.append(so_nguyen)

D={}
for i in range(n):
    D[S[i]]=M[i]
    
item=input()
num=int(input())

if item in D:
    D[item]+=num
else:
    D[item]=num

print(D)