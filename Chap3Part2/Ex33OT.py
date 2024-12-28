n=int(input("n="))
so=n
if 0<=n<=9999:
    if n!=0:
        dem=0
        while n>0:
            n=int(n/10)
            dem+=1
    else:        
        dem=1
    print(so,"co",dem,"chu so")