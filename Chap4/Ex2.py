def Nhap():
    songaynghi=int(input("SNN="))
    return songaynghi
def TinhThuong(n):
    if n==0:
        return 500
    elif n<=2:
        return 300
    elif n<=4:
        return 100
    else:
        return 0
def InKQ():
    while True:
        songaynghi=Nhap()
        if songaynghi>=0:
            print(f"Thuong={TinhThuong(songaynghi)}")
            break
InKQ()