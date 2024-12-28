def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        L.append(int(input()))
    return L
def SND(L):
    count=0
    for i in L:
        if i>0:
            count+=1
    print(f"SND={count}")
def TBCSoNguyenChan(L):
    count=0
    M=[]
    for i in L:
        if i%2==0:
            M.append(i)
    for i in M:
        count+=1
    if count==0:
        print("TBC=0")
    else:
        TBC=sum(M)/count
        print(f"TBC={TBC}")
    
L=Input()
SND(L)
TBCSoNguyenChan(L)