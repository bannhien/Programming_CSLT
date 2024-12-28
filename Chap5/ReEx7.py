H=[]
n=int(input("n="))
for i in range(n):
    num=int(input())
    H.append(num)
M=[]
for i in H:
    if i not in M:
        M.append(i)
for i in M:
    print(i,end=" ")