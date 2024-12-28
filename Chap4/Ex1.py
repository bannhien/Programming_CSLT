sl=int(input("So luong="))
mh=int(input("Ma hang="))

if mh==1:
    dongia=100  
elif mh==2: 
    dongia=200
else: 
    dongia=300
VAT=sl*dongia*0.05
thanhtien=sl*dongia+VAT
print(f"Phai tra={thanhtien}")