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
    
Keys=[]
for k,v in D.items():
    if v>=150:
        Keys.append(k)
for k in Keys:
    del D[k]

print(D)