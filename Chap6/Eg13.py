# Sap xep Dict theo value
# Cách 1:
myDict = {'a': 10, 'b': 150, 'c': 50, 'd': 200}
# Bước 1: Tạo list Keys, chứa tất cả các phần tử có value>=100
Keys=[]
for k, v in myDict.items():
    if v>=100:
        Keys.append(k)
# Bước 2: Xóa tất cả các phần tử trong myDict, có key nằm trong list Keys
for k in Keys:
    del myDict[k]
    
# Cách 2:
myDict = {'a': 10, 'b': 150, 'c': 50, 'd': 200}
# Tạo bản sao của myDict
DCopy= myDict.copy()
for k,v in DCopy.items():
if v>=100:
del(myDict[k])
print(myDict)