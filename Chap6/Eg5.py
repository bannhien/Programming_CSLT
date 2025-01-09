def NhapMatHang():
    H={}
    mahang=int(input("Ma hang: "))
    ten=str(input("Ten hang: "))
    sl=int(input("So luong: "))
    ngay=input("Ngay nhap: ")
    nguoi=input("Nguoi nhap: ")
    H={"mahang": mahang,
       "ten": ten,
       "so luong": sl,
       "ngay nhap": ngay,
       "nguoi nhap": nguoi}
    return H

# def NhapHang():
#     n=int(input("So luong mat hang: "))
#     MatHang={}
#     for i in range(n):
#         H,ma=NhapMatHang()
#         MatHang[ma]=H
#     print(MatHang)
    
# NhapHang()

def NhapHang():
    n=int(input("n="))
    MatHang={}
    for i in range(n):
        H=NhapMatHang()
        MatHang[i+1]=H
    print(MatHang)
    
NhapHang()