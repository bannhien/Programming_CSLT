A=[]
for i in range(10):
    num=int(input())
    A.append(num)
B=[]
B=A.copy()
for i in range(0,10,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for i in B:
    print(i,end=" ")