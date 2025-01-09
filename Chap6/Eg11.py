Students = {
"name": "An",
"age": 18,
"class": "Basic Programming"}
x = Students.pop("class")
print(x)
print(Students)

myDict = dict(name = "An", age = 15, country = "Viet Nam")
x = myDict.popitem()
print(x)
print(myDict)

keys=("age","name","class")
d=dict.fromkeys(keys)
print(d)

keys = {'a', 'e', 'i', 'o', 'u' }
value = 'nguyen am'
dict1 = dict.fromkeys(keys, value)
print(dict1)

d={1:10, 2:20, 3:30}
print(d)
d.clear() # d={}
print(d)

d1={1:10, 2:20, 3:30}
d2=d1 # Ánh xạ
d3=d1.copy() # Tạo bản sao
d4=dict(d1) # Tạo bản sao
print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
print("d4:", d4)
d1[1]=100
print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
print("d4:", d4)