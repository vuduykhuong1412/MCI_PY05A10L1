#range(start, stop, step)

# for i in range(1,8,1):
#     if(i%2) == 0:
#         print(i , " ")


# n = int(input("Nhập n ="))
# sum = 0
# for i in range(n):
#     print(i, "")
#     sum = sum + i

# print("Tổng các số từ 1 đến ", n, "là :", sum)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Vòng lặp for
fruits =["apple", "orange", "tomato", "kiwi"]
for j in fruits:
    print(j)

#String
message = 'She talk "Say good bye"'
message = "She talk 'Say hello'"

desc = '''Ao thu lạnh lẽo nước trong veo
        Một chiếc thuyền câu bé tẻo teo
        Sóng biếc hơi làn đưa gợi tí
'''

text = "Hôm nay trời nắng chang chang\n Mèo con đi học chẳng mang thứ gì \n Chỉ mang 1 chiếc bút chì"
print(text)

# List
plants = ["Earth", "Mars", "Saturn", "Jupiter"]
print(plants[0])
print(plants[1])
print(plants[-1])
del plants[0]
print(plants)

# Tuple
colors = ("Yellow", "Red", "Green")
listColor = list(colors)
print(listColor)
listColor[0] = "Blue"
colors = tuple(listColor)
print(colors)

# Dictionary
cars ={'brand' : 'Toyota', 'color' : 'Red', 'year': 2024}
# Truy cập giá trị của dictionary
# Cách 1
print(cars["brand"])
print(cars["color"])

# Cách 2
print(cars.get('year'))

# Update item trong dictionary
cars['brand'] = 'BMW'
print(cars)

# Thêm mới 1 item
cars['speed'] = '120km/h'
print(cars)

# xóa item
del cars["speed"]
print(cars)


# Đọc ghi file

f = open("thudieu.txt", "w")
f.writelines("Ao thu lanh leo nuoc trong veo"
             +"\nMot chiec thuyen cau be teo teo"
             +"\nSong biec theo lan hoi goi ti,")

f.close()