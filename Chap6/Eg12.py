myDict = {"name" : "An", "age" : 18, "country" : "Viet Nam"}

# Duyet keys
#Cách 1
for x in myDict.keys():
    print(x)
#Cách 2
for x in myDict: # myDict.keys()
    print(x)
    
# Duyet values   
#Cách 1
for x in myDict.values():
    print(x)
#Cách 2
for x in myDict: # myDict.values()
    print(myDict[x])
    
# Duyet ca hai
for k,v in myDict.items():
    print(k,v)
    
# Sap xep Dict theo key
myDict = {'e': 10, 'a': 9, 'c': 15, 'b': 2, 'd': 32}
# Bước 1: Trích tập key trong myDict
myKeys = list(myDict.keys())
# Hoặc: myKeys= [x for x in myDict.keys()]
# Bước 2: Sắp xếp List myKeys tăng dần
myKeys.sort()
# Bước 3: Tạo dict có thứ tự từ myDict theo trường key
sorted_dict = {x:myDict[x] for x in myKeys}
print(sorted_dict)

# Sap xep Dict theo value
# Cách 1
myDict = {'e': 10, 'a': 9, 'c': 15, 'b': 2, 'd': 32}
# Bước 1: tạo list myValues chứa toàn bộ value của myDict
myValues=list(myDict.values())
# Bước 2: Sắp xếp list myValues tăng dần
myValues.sort() # myValues.sort(reverse=True) --> sắp xếp giảm dần
# Bước 3: Tạo dict từ myDict có thứ tự theo list myValues
sorted_dict={}
for x in myValues:
    for k,v in myDict.items():
        if x==v:
            sorted_dict[k]=v
print(sorted_dict)

# Cách 2
myDict = {'e': 10, 'a': 9, 'c': 15, 'b': 2, 'd': 32}
sorted_dict = dict(sorted(myDict.items(), key=lambda item: item[1]))
# key=lambda item: -item[1]) --> Sắp xếp giảm dần
print(sorted_dict)

