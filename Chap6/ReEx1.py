def Duyettu(cumtu):
    cumtu=cumtu.lower()
    tu=cumtu.split()
    D={}
    for moitu in tu:
        if moitu in D:
            D[moitu]+=1
        else:
            D[moitu]=1
    return D

cumtu=input()
Duyettu(cumtu)