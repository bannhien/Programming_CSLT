def DuyetTu(daytu,dayso):
    tu=daytu.split()
    so=dayso.split()
    so=int(so)
    duyet={}
    for i in range(len(tu)):
        duyet[tu[i]]=so[i]
    return duyet

daytu=input()
dayso=input()
print(DuyetTu(daytu, dayso))