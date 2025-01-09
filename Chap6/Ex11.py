def NhapHang():
    MH = {}
    while True:
        mathang = input()
        if mathang == "":
            break
        sl = int(input())
        MH[mathang] = sl
    return MH

def InMaxMin(Hang):
    max_sl_key = max(Hang, key=Hang.get)
    min_sl_key = min(Hang, key=Hang.get)
    max_sl_value = Hang[max_sl_key]
    min_sl_value = Hang[min_sl_key]
    print(max_sl_key, max_sl_value)
    print(min_sl_key, min_sl_value)

def SapXepTheoTen(Hang):
    sorted_Hang = dict(sorted(Hang.items()))
    print(sorted_Hang)

def XoaMatHang(Hang):
    keys_to_delete = [key for key, value in Hang.items() if value <= 10]
    for key in keys_to_delete:
        del Hang[key]
 
    print(Hang)

def TimMatHang(Hang):
    ten_mathang = input()
    if ten_mathang in Hang:
        print(Hang[ten_mathang])
    else:
        print("Khong tim thay")


# Yêu cầu a
Hang = NhapHang()
print(Hang)

# Yêu cầu b
InMaxMin(Hang)

# Yêu cầu c
SapXepTheoTen(Hang)

# Yêu cầu d
XoaMatHang(Hang)

# Yêu cầu e
TimMatHang(Hang)
