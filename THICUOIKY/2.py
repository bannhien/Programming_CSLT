while True:
    st=input()
    if st=="":
        break
    u=""
    for ch in st:
        if ch=="Q":
            u+="9"
        elif ch=="X":
            u+="0"
        elif ch=="S":
            u+="1"
        elif ch=="K":
            u+="6"
        elif ch=="V":
            u+="8"
        else:
            u+=ch
            
    print(u)