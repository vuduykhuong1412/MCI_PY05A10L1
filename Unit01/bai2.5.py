month = int(input("Nhập tháng = "))
if month in [1,2,3]:
    print('Mùa xuân')
elif month in [4,5,6]:
    print('Mùa hè')
elif month in [7,8,9]:
    print('Mùa thu')
elif month in [10,11,12]:
    print('Mùa đông')
else:
    print('Không hợp lệ')