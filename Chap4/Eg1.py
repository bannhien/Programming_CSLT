def Nhap():
    print("Nhap mot so nguyen:")
    n=int(input("n="))
    return n
def Tinh(n):
    S=0
    for i in range (1,n+1):
        S+=i
    return S
def InKQ(n,S):
    print(f"Tong của {n} so nguyen duong dau tien={S}")
    
n=Nhap()
S=Tinh(n)
InKQ(n,S)