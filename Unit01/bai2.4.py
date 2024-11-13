a = int(input("Số thứ nhất = "))
b = int(input("Số thứ hai = "))
c = int(input("Số thứ ba = "))
d = int(input("Số thứ tư = "))

if (a>b and a>c and a>d):
    print('Max =', a)
elif (b>a and b>c and a>d):
    print('Max =', b)
elif (c>a and c>b and c>d):
    print('Max =', c)
elif (d>a and d>b and d>c):
    print('Max =', d)