def Nhap():
    n=int(input("n="))
    return n
def KiemTraSNT(n):
    if n<=2 or n>=1000:
        return False
    for i in range (2,n+1):
        if n%i==0:
            return False
    return True
def InKQ(n):
    if KiemTraSNT(n):
        print(f"{n} la SNT")
    else:
        print(f"{n} khong la SNT")
        
n=Nhap()
InKQ(n)
