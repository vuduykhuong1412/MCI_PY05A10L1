import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Kiểm tra tam giác đều
def is_equilateral(a, b, c):
    return a == b == c

# Kiểm tra tam giác cân
def is_isosceles(a, b, c): 
    return a == b or b == c or a == c

# Kiểm tra tam giác vuông
def is_right(a, b, c):
    edges = sorted([a, b, c])
    return math.isclose(edges[0]**2 + edges[1]**2, edges[2]**2)

def triangle_area(a, b, c):
    if is_equilateral(a, b, c):
        # Tính diện tích tam giác đều
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    elif is_right(a, b, c):
        # Tính diện tích tam giác vuông
        edges = sorted([a, b, c])
        return edges[0] * edges[1] / 2
    elif is_isosceles(a, b, c):
        # Tính diện tích tam giác cân
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        # Tính diện tích tam giác thường
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if is_triangle(a, b, c):
    if is_equilateral(a, b, c):
        print("Tam giác đều.")
    elif is_right(a, b, c):
        print("Tam giác vuông.")
    elif is_isosceles(a, b, c):
        print("Tam giác cân.")
    else:
        print("Tam giác thường.")
    
    # Tính diện tích tam giác
    area = triangle_area(a, b, c)
    print(f"Diện tích của tam giác là: {area:.2f}")
else:
    print("Ba cạnh không tạo thành một tam giác")

