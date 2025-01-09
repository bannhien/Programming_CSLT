# Nhập vào 3 xâu st1, st2, st3
st1 = input("st1= ")
st2 = input("st2=")
st3 = input("st3=")

# In lên màn hình vị trí đầu tiên st2 xuất hiện trong st1
index = st1.find(st2)
if index != -1:
    print(f"Vi tri xuat hien st2: {index}")

# Thay thế tất cả các xâu st2 bằng st3
result = st1.replace(st2, st3)

# In lên màn hình xâu kết quả
print(f"Xâu kết quả: {result}")
