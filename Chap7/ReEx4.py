nhap=input()
A=nhap.split(",")
UniqA=[]
for i in A:
    if i not in UniqA:
        UniqA.append(i)
        
UniqA.sort()
nhap=",".join(UniqA)
print(nhap)