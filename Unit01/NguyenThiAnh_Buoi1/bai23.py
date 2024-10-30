month = int(input())

if month == 2:
    print("Tháng 2 có 28 hoặc 29 ngày.")
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} có 30 ngày.")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} có 31 ngày.")
else:
    print("Không  hợp lệ")
