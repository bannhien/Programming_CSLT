def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    s=1
    if n>=0:
        for i in range (1,n+1,1):
            s*=i
        return s
    else:
        pass
def inkq(n,X):
    print(f"{n}!={X}")
n=nhap()
X=giaithua(n)
inkq(n,X)