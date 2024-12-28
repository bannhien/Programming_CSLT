def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        L.append(int(input()))
    return L

def Search(L):
    max=L[0]
    min=L[0]
    for i in L:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min 
     
def Output(max,min):
    print(max,min)
    
L=Input()
max,min=Search(L)
Output(max,min)