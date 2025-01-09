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
    
V=list(D.values())
V.sort()
sorted_D={}
for x in V:
    for k,v in D.items():
        if x==v:
            sorted_D[k]=v
print(sorted_D)            