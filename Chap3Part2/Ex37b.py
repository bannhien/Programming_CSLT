while True:
    n=int(input())
    s=1
    if n>=0:
        for i in range (1,n+1,1):
            s*=i
        print(s)
    else:
        break
        