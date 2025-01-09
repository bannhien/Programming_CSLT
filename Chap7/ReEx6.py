nhap=input().split(",")
N=[]
for i in nhap:
    a=int(i,2)
    if a%3==0:
        N.append(i)
print(",".join(N))