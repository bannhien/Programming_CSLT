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

sort_D=dict(sorted(D.items(),key=lambda item: item[1]))
print(sort_D)