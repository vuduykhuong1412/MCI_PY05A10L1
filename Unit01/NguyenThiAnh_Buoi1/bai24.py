# Nhập 4 số từ bàn phím
a = int(input("Số thứ nhất: "))
b = int(input("Số thứ hai: "))
c = int(input("Số thứ ba: "))
d = int(input("Số thứ tư: "))

# Tìm số lớn nhất bằng cách so sánh
max_value = a

if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
if d > max_value:
    max_value = d

print(f"Số lớn nhất là: {max_value}")
