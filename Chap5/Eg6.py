def Nhap():
    L=[]
    for i in range(10):
        so=int(input())
        L+=[so]
    x=int(input("x="))
    return L,x

def Thayso(L,x):
    for i in range (len(L)):
        if L[i]==5:
            L[i]=x
            
def Xoa(L,x):
    i=0
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i+=1
def InKQ(L):
    for x in L:
        print(x,end=", ")
        
L=[1,2,3,4,5,5,5,8,9,5]
x=10
Thayso(L,x)
InKQ(L)
Xoa(L,x)
InKQ(L)