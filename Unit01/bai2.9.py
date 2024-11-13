n = int(input("Nhập một số nguyên = "))
total = 0  # khởi tạo biến tổng
while n > 0:
    digit = n % 10
    total += digit
    n = n//10
print(f"Tổng các chữ số trong số là: {total}")