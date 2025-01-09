def KTpass(n):
    n="abc"
    if (len(n)<8) or (n.isalpha()) or (n.isnumeric()) or (n.islower()) or (n.isupper()):
        return True
    else:
        return False
    
while True:
    strPass=input()
    if KTpass(strPass):
        print("Hop le")
        break
    else:
        print("Khong hop le")