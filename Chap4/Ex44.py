def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def max3(a,b,c):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    return max
def inkq(max):
    print(f"So lon nhat la: {max}")
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)