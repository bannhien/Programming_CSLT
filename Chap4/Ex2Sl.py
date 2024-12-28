def Nhap():
    n=int(input("n="))
    return n
def KiemTraSNT(num):
    for i in range (2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def InKQ(n):
    count=0
    num=2
    while count<n:
        if KiemTraSNT(num):
            print(num,end=", ")
            count+=1
        num+=1
        
n=Nhap()
InKQ(n)