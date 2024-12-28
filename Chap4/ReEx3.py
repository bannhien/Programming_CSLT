import math
def nhap():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c):
    delta=b*b-4*a*c
    x1=0
    x2=0
    if delta<0:
        print("Phuong trinh vo nghiem")
    elif delta==0:
        x=-a/(2*b)
        print("Phuong trinh co nghiem kep")
        inkq(x)
    else:
        x1=(-a+math.sqrt(delta))/(2*b)
        x2=(-a-math.sqrt(delta))/(2*b)
        print("Phuong trinh co hai nghiem")
        inkq(x1,x2)
def inkq(x1,x2=None):
    if x2 is None:
        print(f"x1=x2={x1}")
    else:
        print(f"x1={x1}")
        print(f"x2={x2}")

a,b,c=nhap()
giaipt(a, b, c)