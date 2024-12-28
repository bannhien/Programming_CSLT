def PhepCong(x,y=None):
    if y==None:
        return x
    else:
        return x+y
    
kq1=PhepCong(5)
kq2=PhepCong(5,2)
print(kq1,kq2)

def PhepCong(x,y=None):
    return x+y
    
kq3=PhepCong(5,2)
kq4=PhepCong(x=5,y=2)
kq5=PhepCong(x=2,y=5)
print(kq3,kq4,kq5)