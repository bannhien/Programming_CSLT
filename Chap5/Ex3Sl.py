def Nhap():
    x=int(input())
    n=int(input())
    L=[]
    for i in range (n):
        z=int(input())
        L.append(z)
    return x,n,L
def delete(L,x):
    M=[]
    for z in L:
        if x!=z:
            M.append(z)
    return M

x,n,L=Nhap()
M=delete(L,x)
print(M)