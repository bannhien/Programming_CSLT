def Nhap():
    x=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        z=int(input())
        L.append(z)
    return x,n,L
def search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return i
    return None

x,n,L=Nhap()
kq=search(L,x)
print(kq)