D = {}
while True:
    nhap = input()

    if nhap == "":
        break

    item_ten, item_so = nhap.split()
    item_so = int(item_so)


    D[item_ten] = item_so


ten_mat_hang = input()

# Kiểm tra xem mặt hàng cần cập nhật có tồn tại trong dictionary không
if ten_mat_hang in D:
    # Cộng thêm 100 vào số lượng của mặt hàng
    D[ten_mat_hang] += 100

# In ra cấu trúc dictionary sau khi xử lý
print(D)
