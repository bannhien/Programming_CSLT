n=int(input())
S=[]
M=[]
for i in range(n):
    item=input()
    S.append(item)
for i in range(n):
    num=int(input())
    M.append(num)

D={}
for i in range(n):
    D[S[i]]=M[i]

print(S)
print(M)
print(D)