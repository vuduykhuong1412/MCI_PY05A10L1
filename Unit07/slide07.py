import pandas as pd
import numpy as np


# PIVOT TABLE


# Tạo DataFrame mẫu
data1 = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [200, 150, 300, 400, 250, 180, 320, 410],
    'Quantity': [20, 15, 30, 40, 25, 18, 32, 41]
}

df = pd.DataFrame(data1)

# Tạo bảng pivot_table
pivot = pd.pivot_table(
    df,
    values=['Sales', 'Quantity'],  # Cột cần tính toán
    index='Region',                # Cột làm chỉ mục
    columns='Product',             # Cột làm phân loại
    aggfunc='sum',                 # Hàm tính toán (sum, mean, etc.)
    fill_value=0                   # Giá trị mặc định nếu thiếu
)

print("Pivot Table:")
print(pivot)

# TIME-SERIES DATA

# Tạo DataFrame mẫu với dữ liệu thời gian
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = {
    'Date': date_rng,
    'Sales': np.random.randint(100, 500, size=len(date_rng))  # Random sales data
}

df = pd.DataFrame(data)

# Chuyển cột 'Date' thành kiểu datetime và đặt làm chỉ mục
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Resample dữ liệu theo tuần và tính tổng doanh số
weekly_sales = df['Sales'].resample('W').sum()

print("Original Data:")
print(df)

print("\nWeekly Sales (Resampled):")
print(weekly_sales)



# OTHER
from datetime import datetime

date_strs = ['2024-09-11 13:40:50', '2024-09-10 00:00:00']
print(pd.to_datetime(date_strs))

idx = pd.to_datetime([*date_strs, None])
print(idx)

print(idx[1])
print(pd.isnull(idx))

dates = [datetime(2024, 9, i) for i in range(1,7)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
print(ts.index)

# Time-Series with Pandas
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('2024-09-11', periods=1000))
print(longer_ts)

# Select data by year and month
print(longer_ts['2024-09'])

# Select data by year
print(longer_ts['2024'])


# BAI 7
# Tại sao Kỹ thuật tính năng lại quan trọng:
# - Dữ liệu ban đầu ở dạng thô và chưa sẵn sàng cho mục đích phân tích/mô hình hóa
# - Kỹ thuật tính năng là quá trình sử dụng kiến ​​thức về miềncủa dữ liệu để tạo (hy vọng là) các tính năng Chiếm 80% - 90% dự án khoa học dữ liệu

# Kỹ thuật tính năng là gì?
# - Ngay cả tập dữ liệu thô cũng có các tính năng. Hầu hết thời gian, dữ liệu sẽ ở dạng bảng.
# - Mỗi cột là một tính năng. Nhưng các tính năng này có thể không tạo ra kết quả tốt nhất từ ​​thuật toán.
# - Việc sửa đổi, xóa và kết hợp các tính năng này sẽ tạo ra một tập hợp mới có khả năng đào tạo thuật toán tốt hơn.
# - Kỹ thuật tính năng trong học máy không chỉ là lựa chọn các tính năng phù hợp và chuyển đổi chúng.
# - Kỹ thuật tính năng không chỉ chuẩn bị tập dữ liệu để tương thích với thuật toán mà còn cải thiện hiệu suất của các mô hình học máy.


# Dữ liệu gốc: ranh giới phi tuyến tính và
# không thuận tiện cho nhiều
# thuật toán học máy


# Dữ liệu phái sinh: ranh giới tuyến tính và sẽ
# hoạt động với hầu hết các thuật toán học máy


#  Một quy trình làm việc chung để phát triển mô hình:
#  sử dụng pandas để tải và dọn dẹp dữ liệu.
#  một thư viện mô hình hóa để xây dựng mô hình.
#  Điểm tiếp xúc giữa pandas và các thư viện phân tích khác


# Mảng NumPy
#  - Để chuyển đổi DataFrame thành mảng NumPy:
#  - Sử dụng thuộc tính .values:
#  - Để chuyển đổi trở lại DataFrame: truyền một ndarray hai chiều với các
#    tên cột tùy chọn


data = pd.DataFrame({
    'x0' : [1,2, 3, 4, 5],
    'x1' : [0.01, -0.01, 0.25, -4.1, 0.],
    'y' : [-1.5, 0.0, 3.6, 1.3, -2.0] 
})

print(data)
print(data.columns)
print(data.values)

df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
print(df2)

df3 = data.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
print(df3)

model_cols = ['x0', 'x1']
print(data.loc[:, model_cols].values)
print(data[model_cols].values)



data['category'] = pd.Categorical(
    ['a', 'b', 'a', 'a', 'b'],
    categories=['a', 'b'])

print(data)


dummies = pd.get_dummies(data.category, prefix='category')
print(dummies)

data_with_dummies = data.drop('category', axis=1).join(dummies)
print(data_with_dummies)

# CREATING MODEL DESCRIPTIONS  WITH PATSY