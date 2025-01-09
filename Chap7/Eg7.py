def Nhapso(thongbao):
    while True:
        n=input(thongbao)
        if n.isnumeric():
            return int(n)
        
a=Nhapso("a=")
b=Nhapso("b=")
print(f"a+b={a+b}")
