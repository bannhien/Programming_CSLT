s=input()
kq=[]
for i, char in enumerate(s):
    if char.isupper() and i!=0:
        kq.append(" ")
    kq.append(char)
print("".join(kq))