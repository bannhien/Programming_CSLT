def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    s=1
    if n>1:
        for i in range(1,n+1):
            s*=i
    elif n==1:
        s=1
    return s
def inkq(n,s):
    print(f"{n}!={s}")
    
n=nhap()
s=giaithua(n)
inkq(n,s)