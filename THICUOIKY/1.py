def Nhap():
    n=int(input())
    return n
def KiemTraSNT(num):
    for i in range (2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def InKQ(n):
    count=0
    for i in range(2,n+1):
        if KiemTraSNT(i):
            count+=1
    print(count)
    
n=Nhap()
InKQ(n)