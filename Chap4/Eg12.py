def spam():
    global eggs #global khai báo 1 biến cục bộ thành toàn cục
    eggs="spam"
    
eggs="global"
spam()
print(eggs)

