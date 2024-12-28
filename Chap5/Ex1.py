def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        L.append(int(input()))
    
    x=int(input("x="))
    return L,x 

def FirstAndLast(L):
    if len(L)==1:
        print([L[0]])
    else:
        print([L[0],L[-1]])

def Search(L,x):
    if x in L:
        print(True)
    else:
        print(False)

L,x=Input()
FirstAndLast(L)
Search(L,x)