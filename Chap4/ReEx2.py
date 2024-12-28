def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    for i in range (2,n+1,2):
        print(i,end=" ")
while True:
    n=nhap()
    inkq(n)
    print()
    tieptuc=input("Tiep tuc khong?")
    if tieptuc=="k" or tieptuc=="K":
        break