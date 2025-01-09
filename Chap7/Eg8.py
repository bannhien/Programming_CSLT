def KT(n):
    hoa = 0
    thuong = 0
    so = 0 
    pw = 0
    for i in n:
        if i>="A" and i<="Z":
            hoa = 1
        elif i>="a" and i<="z":
            thuong =  1
        elif  i>="0" and i<="9":
            so =  1
    if len(n)>=8 and thuong==1 and hoa==1 and so==1:
        pw=1
    else:
        pw=0
    return pw

def inkq(kq):
    if kq==1:
        print("Hop le")
    if kq==0:
        print("Khong hop le")
        
password=input()
n=KT(password)
inkq(n)