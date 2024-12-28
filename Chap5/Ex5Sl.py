def Nhap():
    x=int(input())
    y=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        z=int(input())
        L.append(z)
    return x,y,n,L
def replace(L,x,y):
    for i in range(len(L)):
        if x==L[i]:
            L[i]=y
    return L
x,y,n,L=Nhap()
replace(L,x,y)
print(L)