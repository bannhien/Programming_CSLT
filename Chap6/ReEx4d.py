n=int(input())
S=[]
M=[]
for i in range(n):
    chuoi=input()
    S.append(chuoi)
for i in range(n):
    so=int(input())
    M.append(so)

D={}
for i in range(n):
    D[S[i]]=M[i]

print(sum(D.values()))