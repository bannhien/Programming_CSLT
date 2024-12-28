def Nhap():
    L=[]
    n=int(input("n="))
    for i in range(n):
        num=int(input())
        L.append(num)
    x=int(input("x="))
    return x,L

def CauA(L,x):
    if x in L:
        L.remove(x)
        print(L)

def CauB(L,x):
    while x in L:
        L.remove(x)
    print(L)

x,L=Nhap()
CauB(L,x)