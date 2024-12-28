def Input():
    L=[]
    n=int(input("n="))
    for i in range(n):
        num=int(input())
        L.append(num)
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    if len(L)==1:
        print(L[0])
    else:
        print([L[0],L[-1]])
def Search(L,x):
    if x in L:
        print(True)
    else:
        print(False)
        
L,x=Input()
FirstAndLast(L)
Search(L, x)