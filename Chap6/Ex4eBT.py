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
    
keys=[]
for k,v in D.items():
    if v>=150:
        keys.append(k)
for k in keys:
    del D[k]
print(D)