kw=int(input("Tieu thu="))
if 1<=kw<=100:
    thanhtien=kw*550
elif 101<=kw<=150:
    thanhtien=100*550+(kw-100)*750
elif 151<=kw<=200:
    thanhtien=100*550+50*750+(kw-150)*950
elif 201<=kw:
    thanhtien=100*550+50*750+50*950+(kw-200)*1350
    
tienthuc=thanhtien*1.1
print(f"Phai tra={tienthuc}")