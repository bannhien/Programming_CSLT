n=int(input("n="))
L=[]
for i in range (1,n+1):
    L.append(int(input()))
    
snd=0
for i in L:
    if i>0:
        snd=snd+1
print("SND=",snd,sep="")

tong=0
dem=0
for i in L:
    if i%2==0:
        tong=tong+i
        dem=dem+1
if dem>0:
    tbc=tong/dem
    print("TBC=",tbc,sep="")
else:
    print("TBC=0")