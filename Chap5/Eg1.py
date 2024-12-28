nums=[1,2,3,4,5]
print(nums[0:3])

num1s=[item for item in range (1,6)]
print(num1s)

matrix=[[x,x+1,x+2] for x in range (1,10,3)]
print(matrix)

char=list("Python")
print(char)

print(char[0])
print(char[-1])

L=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(L[1][2])
print(L[1])

nums=nums+[3,4]
print(nums)

nums=nums*2
print(nums)

num2s=[5,3,2,4,6,7,8]
print(max(num2s))
print(min(num2s))
del(num2s[1])
print(num2s)

students=["An","Binh","Lan","Thanh","Minh"]
for x in students:
    print(x,end=", ")
    
for x in range(len(students)):
    print(students[x],end=", ")
    
