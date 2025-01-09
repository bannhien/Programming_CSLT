D={"Cafe": 10, "Bia": 15, "My Quang": 20, "Nuoc ngot": 17}

n=int(input("n="))
DCopy= D.copy()
for k,v in DCopy.items():
    if v<=n:
        del(D[k])
print(D)