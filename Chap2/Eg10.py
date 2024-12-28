#viết chương trình nhập vào từ bàn phím một số thực n, Cho viết n là "Số âm" hay "số dương"
num=float(input("num="))
if num<0:
    print(f"{num} la so am")
elif num==0:
    print(f"{num} khong la so am va so duong")
else:
    print(f"{num} la so duong")