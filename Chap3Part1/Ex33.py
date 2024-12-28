x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if ch=="+":
    print(f"{x}+{y}={round(x+y,1)}")
elif ch=="-":
    print(f"{x}-{y}={round(x-y,1)}")
elif ch=="*":
    print(f"{x}*{y}={round(x*y,1)}")
elif ch=="/":
    if y==0:
        print("Khong hop le")
    else:
        print(f"{x}/{y}={round(x/y,1)}")
else:
    print("Khong hop le")