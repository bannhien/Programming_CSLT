def Nhap():
    x=int(input())
    L=[]
    for i in range (1,x+1):
        z=int(input())
        L.append(z)
    return x,L
def count(L):
    dem=0
    for i in L:
        dem+=1
    return dem
x,L=Nhap()
dem=count(L)
print(dem)