spam = {"color": "red", "age": 42}
#truy xuất tập values
for x in spam.values():
    print(x)
    
#Truy xuất về tập keys
for x in spam.keys():
    print(x)
#Truy xuất cả keys lẫn items
for x in spam.items():
    print(x)
    
for k,v in spam.items():
    print(k,v)