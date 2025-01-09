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
    
st=input()
x=int(input())

if st in D:
    D[st]+=x
else:
    D[st]=x

print(D)