L=[1,2,5,4,5,6,5,8,9]
print(L.index(5))

names =[1,2,3,4,5,6]

names.append(6)
print(names)

names.insert(0,7)
print(names)

names.insert(-1,8)
print(names)

names.insert(100,5)
print(names)

def remove_all_fives(lst):
    while 5 in lst:
        lst.remove(5)
X=[1, 2, 3, 5, 5, 5, 8, 9, 5]
remove_all_fives(X)
print(X)

numbers = [1, 2, 3, 4, 5]
numbers.sort() # or: numbers.sort(reverse=False)
print(numbers)
numbers.sort(reverse=True)
print(numbers)

L=["Binh", "An","Nam","Anh", "A"]
L.sort()
print(L)
L.reverse()
print(L)

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 2, 5]
print(numbers.count(2))
print(numbers.count(5))
print(numbers.count(10))

numbers = [1, 2, 3, 4, 5]
x=numbers.pop(2)
print(numbers)
print(x)

numbers = [1, 2, 3, 4, 5]
x=numbers.pop()
print(numbers)
print(x)