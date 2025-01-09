nhap=input()
A=nhap.split(" ")
n=int(input())
for i in range(len(A)):
    if int(A[i])==n:
        print(i+1)
if n not in A:
    print(0)