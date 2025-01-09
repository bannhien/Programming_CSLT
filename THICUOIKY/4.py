nhap=[int(s) for s in input().split()]
def DemSoAm(nhap):
    count=0
    for i in nhap:
        if i<0:
            count+=1
    return count

def TongSoDuong(nhap):
    S=0
    for i in nhap:
        if i>0:
            S+=i
    return S

def InKQ(count,S):
    print([count,S])
    
count=DemSoAm(nhap)
S=TongSoDuong(nhap)
InKQ(count, S)