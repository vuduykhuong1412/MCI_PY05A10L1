n = int(input("Nhập một số: "))

# Biến để lưu trữ tổng
sum_of_numbers = 0

# Dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1, n + 1):
    sum_of_numbers += i #sum_of_numbers += i sẽ cộng giá trị của i vào tổng tương tự như: sum_of_numbers = sum_of_numbers + i

# In kết quả
print("Tổng các số từ 1 đến", n, "là:", sum_of_numbers)