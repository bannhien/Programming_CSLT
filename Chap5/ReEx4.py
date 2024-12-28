A=[]
n=int(input("n="))
for i in range(n):
    num=int(input())
    A.append(num)
A.reverse()
print(A)
B=[]
B=A.copy()
B.sort()
print(B)