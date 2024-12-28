def Nhap():
    x=int(input())
    k=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        z=int(input())
        L.append(z)
    return x,k,n,L
def add(L,x,k):
    L=L[:k] + [x]+ L[k:]
    return L

x,k,n,L=Nhap()
L=add(L,x,k)
print(L)