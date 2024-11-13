n = int(input("Nhập một số nguyên: "))

# Biến để lưu trữ số đảo ngược
reversed_number = 0

# Sử dụng vòng lặp while để đảo ngược số
while n != 0:
    digit = n % 10            # Lấy chữ số cuối cùng của n
    reversed_number = reversed_number * 10 + digit  # Cập nhật số đảo ngược
    n //= 10                   # Loại bỏ chữ số cuối cùng khỏi n

# In ra số đảo ngược
print("Số đảo ngược là:", reversed_number)