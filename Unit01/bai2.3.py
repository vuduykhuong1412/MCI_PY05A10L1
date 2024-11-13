month = int(input("Nhập tháng = "))
a = [4,6,9,11]
b = [1,3,5,7,8,10,12]
c = [2]
if(month in b):
    print("Tháng", month, "có 31 ngày")
elif(month in a):
    print("Tháng", month, "có 30 ngày")
elif(month in c):
    print("Tháng", month, "có 28 hoặc 29 ngày")
else:
    print('Không hợp lệ')