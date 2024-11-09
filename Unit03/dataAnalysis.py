import numpy as np
import pandas as pd
import csv

# path = 'winequality-red.csv'
# # data = pd.read_csv(path)
# # print(data.head())

# # doc thong tin file winequality-red.csv va luu thanh 1 mang
# with open(path, 'r') as f:
#     wines = list(csv.reader(f, delimiter=';'))

# # tim cac hang co chat luong ruou > 7
# high_quality_wines = wines[wines['quality'] > 7]
# print(high_quality_wines)

# #print(wines)

# # hien thi 5 hang dau va 5 hang cuoi cua du lieu
# #print(wines[:5])
# #print(wines[-5:])

# # tinh trung binh chaat luong cua ruou
# # qualities = [float(item[-1]) for item in wines[1:]]
             
# # total_average = sum(qualities)/ len(qualities)

# # print(total_average)

# # xac dinh kich thuoc mang
# #print(wines.shape)

# # tim cac hang co chat luong ruou > 7
# #df =pd.DataFrame(wines)
# # high_quality = wines[:,11] > 7
# # dt = wines[high_quality,:][:3,:]

# # print(dt)

# #data_red = np.genfromtxt(path, delimiter=';', skip_header=1)

# # Xac dinh kich thuoc
# #print(data_red.shape)

path = 'Breast_cancer_data.csv'

df =pd.read_csv(path)
print(df.dtypes)
print(df.describe())
#df.groupby(by =['class', 'doctor_name']).size()
print(df.isna().sum())
df = df.dropna(axis=0, how='any')
print(df)
print(df.nunique())
# check dubplicate
print(df[df.duplicated(subset='mean_radius', keep=False)].sort_values('mean_radius'))

# doc file html
print("=======================================")
tables = pd.read_html("fdic_failed_bank_list.html")
len(tables)
failures = tables[0]
print(failures.head())

print("=======================================")
close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())