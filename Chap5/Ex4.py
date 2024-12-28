n=int(input("n="))
A=[] 
for i in range (1,n+1):
    A.append(int(input()))

A.reverse()
B=[]
B=A.copy()
print(B)
B.sort()
print(B)
