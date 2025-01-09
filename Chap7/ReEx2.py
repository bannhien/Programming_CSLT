def nhap():
    s=input().strip()
    return s
def xuly(s):
    a=s.split()
    s=" ".join(a)
    s=s[0].title()+s[1:].lower()
    s=s.replace(" ,",",").replace(" ;", "; ").replace(" :", ": ").replace(" .", ". ")
    print(s)
s=nhap()
xuly(s)