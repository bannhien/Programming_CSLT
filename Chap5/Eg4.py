def replace_value(lst, x):
    result_a = [x if num == 5 else num for num in lst]
    print(", ".join(map(str, result_a)))
    
def remove_value(lst, x):
    result_b = [num for num in lst if num != x]
    print("Cau b:")
    print(", ".join(map(str, result_b)))

nums = []
for i in range(10):
    num = int(input())
    nums.append(num)

x = int(input("x="))

replace_value(nums, x)