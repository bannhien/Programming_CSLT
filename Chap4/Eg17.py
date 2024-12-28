def Nhap():
   n=int(input("n="))
   return n


def LaSNT(x):
   # 1 và x: i=2 --> (x-1)
   for i in range(2,x):
      if x%i==0:  #x chia het cho i
         return False   #x khong la SNT
   return True


def DaySNT(n):
   for x in range(2,n+1):  # x=2..n
      if LaSNT(x)==True:
         print(x,end=", ")


n=Nhap()
DaySNT(n)
