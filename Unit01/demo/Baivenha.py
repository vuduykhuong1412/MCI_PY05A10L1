# Bài  2.1: Tính diện tích của các lại tam giácgiá

# Bài 2.2: Kiểm tra số trong tuần
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input ("Nhập số liệu:"))
print (a)

if a < 2:
    print(" không là ngày trong tuần")
elif a > 8:
        print(" không là ngày trong tuần")
else:
    print(" là ngày trong tuần")

# Bài 2.3: Nhập số có tháng tương ứng và số ngày tương ứng của tháng đó

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = int(input ("Tháng: ")
print (a))

if a==2:
    print("Tháng đó có 28 hoặc 29 ngày)")
elif a== 4 or 6 or 9 or 11:
    print("Tháng đó có 30 ngày")
else:
    print("Tháng đó có 31 ngày")

# Bài 2.4: Tìm max trong 4 số

# Bài 2.5: Viết chương trình nhập 

# Bài 2.6: Tính tiền bằng số km đã nhập theo yêu cầu

a = float(input ("Số km là: ")) #a là biến của số km đi đường
print (a)

if a < 1: 
    print ("Số tiền phải trả là 5.000 vnđ")
elif a >= 1 and a <5: 
    b = a*4500+5000
    print ("Số tiền phải trả là", b)
elif a >=5 and a <= 120:
    b = a*3500+4500*4+5000
    print ("Số tiền phải trả là", b)
else:
    b = ((a*3500+4500*4+5000)*1/10)
    print ("Số tiền phải trả là", b) 

# Bài 2.7: Tính tiền sử dung máy tính (1h = 5000đ)

a = float(input ("Thời gian sử dụng máy tính: ")) #(1h = 5000)
a1 = float(input ("Thời gian sử dụng máy tính: ")) #(1h = 5000)
a2 = float(input ("Thời gian sử dụng máy tính: ")) #(1h = 5000)

print (a)
print (a1)
print (a2)

#Theo khung giờ từ 0h đến 7h sáng
if 0 <= a <= 7: #Khung giờ trước 7h sáng
    b = a*5000*300
    print ("Số tiền sử dụng máy tính là ", b)
else: #Khung giờ sau 7h sáng
    b = (a*5000*300*60)/0.15
    print ("Số tiền sử dụng máy tính là ", b)

if 7 < a1 <= 17: #Khung giờ trước 6h chiều
    b1 = (a1*5000*400)/0.1
    print ("Số tiền sử dụng máy tính là ", b1)
else: #Khung giờ sau 6h chiều
    b1 = (a1*5000*400*60)/0.1
    print ("Số tiền sử dụng máy tính là ", b1)

if 17 < a2 <= 24: #Khung giờ trước 4h chiều
    b2 = (a2*5000*350)
    print ("Số tiền sử dụng máy tính là ", b2)
else: #Khung giờ sau 4h chiều
    b2 = (a2*5000*350*60)/0.12
    print ("Số tiền sử dụng máy tính là ", b2)