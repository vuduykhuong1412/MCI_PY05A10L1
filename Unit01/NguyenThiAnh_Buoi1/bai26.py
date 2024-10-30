km = float(input("Số km: "))

if km <= 1:
    tien = 5000
elif km <= 5:
    tien = (km - 1) * 4500 + 5000
elif km <= 120:
    tien = (km - 5) * 3500 + 4 * 4500 + 5000
else:
    tien = ((km - 5) * 3500 + 4 * 4500 + 5000) * 0.1 

print(f"Số tiền phải trả là: {tien:.0f} đồng")
