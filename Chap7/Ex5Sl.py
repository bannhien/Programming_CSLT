def count_letters_and_digits(input_string):
    letter_count = 0
    digit_count = 0
    
    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
            
    return letter_count, digit_count

# Nhập chuỗi từ người dùng
input_string = input()

# Đếm số chữ cái và chữ số
letters, digits = count_letters_and_digits(input_string)

# In kết quả ra màn hình
print("Chu cai:", letters)
print("Chu so:", digits)
