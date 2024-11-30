from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
# Du lieu duoc tao

#Bài toán: Dự đoán giá nhà dựa trên diện tích (X) và giá thực tế (y)
data = {
    'Area' :[800, 1000, 1200, 1500, 1800],
    'Price':[200, 250, 300, 400, 500]
}

df = pd.DataFrame(data)

# Du lieu dien tich (X)s va gia (y)
X = df[['Area']]
y = df['Price']


# Chia du lieu thanh tap huan luyen va kiem tra
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

# Khoi tao va huan luyen mo hinh
model = LinearRegression()
model.fit(X_train, y_train)

# Du doan gia tri tu du lieu kiem tra
y_predict = model.predict(X_test)

# Hien thi ket qua
print("Giá trị thực tế :", list(y_test))
print("Giá trị dự đoán :", list(np.round(y_predict, 2)))
      