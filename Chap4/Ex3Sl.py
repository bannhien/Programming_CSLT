def NhapSoThucVaToanTu():
    a=float(input("a="))
    b=float(input("b="))
    ch=str(input("Toan tu: "))
    return a,b,ch

def Tinh(a,b,ch):
    if ch=="+":
        return a+b
    elif ch=="-":
        return a-b
    elif ch=="*":
        return a*b
    elif ch=="/":
        if b!=0:
            return a/b
        else:
            pass

def ChayCT():
    while True:
        a,b,ch=NhapSoThucVaToanTu()
        kq=Tinh(a,b,ch)
        print(f"{a}{ch}{b}={kq}")
        lap=str(input("Tiep tuc: "))
        if lap=="T" or lap=="t":
            break
ChayCT()
