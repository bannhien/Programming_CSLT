n=int(input("n="))
L=[]
for i in range (1,n+1):
    L.append(int(input()))

M=[]
for i in L:
    if i not in M:
        M.append(i)

for i in M:
    print(i,end=" ")