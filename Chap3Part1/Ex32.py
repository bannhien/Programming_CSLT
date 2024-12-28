M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    print(f"Phai tra={M1*S}")
elif 101<=S<=150:
    print(f"Phai tra={M1*100+M2*(S-100)}")
else:
    print(f"Phai tra={M1*100+M2*50+M3*(S-150)}")