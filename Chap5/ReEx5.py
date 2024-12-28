n=int(input("n="))
A=[]
for i in range(n):
    num=int(input())
    A.append(num)
tong=0
for i in range(n):
    if i%2!=0:
        tong+=A[i]
print(f"Tong={tong}")