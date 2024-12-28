n=int(input())
u=""
while n>0:
    s=n%10
    if s==0:
        u='A'+u
    elif s==1:
        u='B'+u
    elif s==3:
        u='C'+u
    elif s==4:
        u='D'+u
    elif s==5:
        u='F'+u
    elif s==6:
        u='G'+u
    elif s==7:
        u='H'+u
    elif s==8:
        u='K'+u
    elif s==9:
        u='L'+u
    n=n//10
print(u)