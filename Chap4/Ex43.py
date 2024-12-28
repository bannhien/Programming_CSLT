import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c):
    d=b*b-4*a*c
    x1=0
    x2=0
    if d<0:
        print("Phuong trinh vo nghiem")
    elif d==0:
        x=-b / (2*a)
        print("Phuong trinh co nghiem kep")
        inkq(x)
    else:
        x1=(-b + math.sqrt(d))/(2*a)
        x2=(-b - math.sqrt(d))/(2*a)
        print("Phuong trinh co hai nghiem")
        inkq(x1,x2)
def inkq(x1,x2=None):
    if x2 is None:
        print(f"x1=x2={x1}")
    else:
        print(f"x1={x1}")
        print(f"x2={x2}")
a,b,c=nhap()
giaipt(a,b,c)