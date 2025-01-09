def KTTen(n):
    n="Abc"
    if n.istitle():
        return True
    else:
        return False
def Nhap():
    n=input("Ho ten: ")
    if KTTen(n):
        print("Hop le!!!!")
    else:
        print("Khong hop le!!!")