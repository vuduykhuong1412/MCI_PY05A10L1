import math
km = float(input("Nhập số km = "))

if km == 1:
    tien = 5000
elif 1<= km <= 5:
    tien = (km-1)*4500+5000
elif 5<= km <= 120:
    tien = (km-5)*3500+4500*4+5000
elif km > 120:
    tien = ((km-5)*3500+4500*4+5000)*1/10
print('Tổng số tiền =', tien, 'đồng')