a=float(input())
b=float(input())
c=float(input())
if a>0 and b>0 and c>0 and (a+b)>c and (b+c)>a and (c+a)>b:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a:
        print("Tam giac vuong")
    elif a==b and b==c and c==a:
        print("Tam giac deu")
    else: 
        print("Tam giac loai khac")
else:
    print("Khong hop le")