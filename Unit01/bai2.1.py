import math

def kiemTraTamGiac():
    print("Nhập 3 cạnh tam giác")
    a = float(input("Nhập cạnh a = "))
    b = float(input("Nhập cạnh b = "))
    c = float(input("Nhập cạnh c = "))
    if(a < 0 or b <0 or c <0):
        print("Không tồn tại 3 cạnh tam giác âm")
    elif(a + b < c or b + c < a or c + a < b):
        print("Không thỏa mãn 3 cạnh tam giác")
    else:
        if(a == b and b == c):
            print("3 cạnh là tam giác đều")
        elif(a == b or b == c or c == a):
            print("3 cạnh là tam giác cân")
        elif( a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b):
            print("3 cạnh là tam giác vuông")
        else:
            print("3 cạnh là tam giác thường")

        p = (a + b + c)/2
        s = math.sqrt(p*(p - a)*(p - b)*(p -c))
        print("Diện tích tam giác là : ", s)


kiemTraTamGiac()