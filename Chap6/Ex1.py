def NhapSLHang():
    MH={}
    while True:
        mathang=str(input("mat hang:"))
        if mathang=="":
            break
        sl=int(input("so luong:"))
        MH[mathang]=sl
    return MH

def MaxMin(Hang):
    max_mh=max(Hang, key=Hang.get)
    min_mh=min(Hang, key=Hang.get)
    max_sl=Hang[max_mh]
    min_sl=Hang[min_mh]
    return max_mh,min_mh,max_sl,min_sl

def SapXep(Hang):
    SX=list(Hang.keys())
    SX.sort()
    Sort_dict={x:SX[x] for x in SX}
    return Sort_dict

def Xoa(Hang):
    DCopy=Hang.copy()
    for k,v in DCopy.items():
        if v<=10:
            del(Hang[k])
    return Hang

def Tim(Hang):
    ten_mathang = input()
    if ten_mathang in Hang:
        print(ten_mathang, Hang[ten_mathang])
    else:
        print("Khong tim thay")

Hang = NhapSLHang()
print(Hang)

    # Yêu cầu b
MaxMin(Hang)

    # Yêu cầu c
SapXep(Hang)

    # Yêu cầu d
Xoa(Hang)

    # Yêu cầu e
Tim(Hang)