# Bai toan phan loai xe dua tren so cho ngoi, gia va cong suat
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# tao du lieu mau
data = {
    'Seats' : [2, 4, 4, 4, 6],
    'Price' : [100, 200, 300, 400, 500],
    'Horsepower' : [150, 120, 200, 250, 300],
    'Car Type' :['Sports', 'Sedan', 'SUV', 'SUV', 'Vans']
}

df = pd.DataFrame(data)

# Chuyen doi nhan (Car Type) thanh so
encoder = LabelEncoder()
df['Car Type'] = encoder.fit_transform(df['Car Type'])

# Du lieu X va y
X = df[['Seats','Price', 'Horsepower']]
y = df['Car Type']

# Chia du lieu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khoi tao va huan luyen mo hinh
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Du doan
y_predict = clf.predict(X_test)

# hien thi ket qua
print("Giá trị thực tế :", list(y_test))
print("Giá trị dự đoán :", list(y_predict))