L=[1,2,3,4,5,6,7,8,9]
def CauB(L):
    M=[]
    for i in range (len(L)):
        if i%2!=0:
            M.append(L[i])
    L=M.copy()
    print(L)
CauB(L)