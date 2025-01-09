def NhapMatHang():
    MH={}
    mahang=input("Ma hang: ")
    tenhang=input("Ten hang: ")
    soluong=int(input("So luong: "))
    ngaynhap=input("Ngay nhap: ")
    tennguoinhap=input("Ten nguoi nhap: ")
    MH={
        "Ma hang": mahang,
        "Ten hang": tenhang,
        "So luong": soluong,
        "Ngay nhap": ngaynhap,
        "Ten nguoi nhap": tennguoinhap}
    return MH
# def NhapHang():
#     n=int(input("So luong mat hang: "))
#     Hang={}
#     for i in range(n):
#         H,ma=NhapMatHang()
#         Hang[ma]=H
#     print(Hang)
    
# NhapHang()

def NhapHang():
    n=int(input("So luong mat hang: "))
    Hang={}
    for i in range(n):
        H=NhapMatHang()
        Hang[i+1]=H
    print(Hang)
    
NhapHang()