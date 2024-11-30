import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Tao du lieu gia lap

data = {
    'CustomerID' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Purchases':[5, 10, 12, 8, 20, 7, 15, 25, 30, 40],
    'Spending':[200, 450, 600, 300, 1200, 250, 900, 1500, 2000, 3000]
}

df = pd.DataFrame(data)

# Chuan bi du lieu
X = df[['Purchases', 'Spending']]
# Phan cum khach hang thanh cac nhom: it mua - chi tieu thap, thuong xuyen mua - chi tieu cao
# Ap dung thuat toan kMeans voi cum la 3
kmeans = KMeans(n_clusters= 3, random_state= 42)
df['Cluster'] = kmeans.fit_predict(X)

# Hien thi ket qua
print(df)

# Ve do thi phan cum
plt.scatter(X['Purchases'], X['Spending'], c= df['Cluster'], cmap='viridis')
plt.xlabel('Purchases')
plt.ylabel('Spending')
plt.title('Customer segments')

plt.show()