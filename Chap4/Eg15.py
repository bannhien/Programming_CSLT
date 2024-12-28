def Nhap():
    n=int(input("n="))
    m=int(input("m="))
    return n,m
def InKQ(n=2,m=100):
    for i in range (n,m+1,1):
        if i%2==0:
            print(i)
        
n,m=Nhap()
InKQ(n=2,m=7)