def DuyetTu(cumtu):
    cumtu=cumtu.lower()
    tu=cumtu.split()
    duyet={}
    for moitu in tu:
        if moitu in duyet:
            duyet[moitu]+=1
        else:
            duyet[moitu]=1
    return duyet

cumtu=input()
print(DuyetTu(cumtu))