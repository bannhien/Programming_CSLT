def NhapTTSV():
    SV={}
    maSV=str(input("maSV="))
    tenMH=str(input("tenMH="))
    diemthi=float(input("Diem thi="))
    SV={
        "Ma SV": maSV,
        "Ten mon hoc:": tenMH,
        "Diem thi": diemthi}
    return SV

def NhapSV():
    n=int(input("Nhap so luong sinh vien: "))
    SinhVien={}
    for i in range(n):
        Students=NhapTTSV()
        SinhVien[i+1]=Students
        
    print(SinhVien)
        
NhapSV()