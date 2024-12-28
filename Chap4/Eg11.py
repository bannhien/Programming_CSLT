def Nhap():
    n=int(input("n="))
    return n
def NhapVaDem(n):
    print(f"Nhap {n} so nguyen:")
    s=0
    for i in range(1,n+1):
        x=int(input())
        if x%2==0:
            s+=1
    return s
def InKQ(kq):
    print(f"So chu so chan la: {kq}")
    
n=Nhap()
x=NhapVaDem(n)
kq=InKQ(x)