def DuyetTu(cumtu, cumso):
    tu = cumtu.split()
    so = [int(s) for s in cumso.split()]  # Chuyển từng phần tử trong cumso sang số nguyên
    D = {}
    for i in range(len(tu)):
        D[tu[i]] = so[i]
    return D

daytu = input()
dayso = input()
print(DuyetTu(daytu, dayso))
