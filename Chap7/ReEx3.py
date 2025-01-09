import re
nhap=input()

if len(nhap)<6 or len(nhap)>17:
    kq=False
elif not re.search("[a-z]",nhap) or not re.search("[A-Z]",nhap) or not re.search("[0-9]",nhap) or not re.search("[$ # @]",nhap):
    kq=False
else:
    kq=True
print(kq)