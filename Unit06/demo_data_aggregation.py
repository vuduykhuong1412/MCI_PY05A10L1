import pandas as pd
import numpy as np

df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2':['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randn(5),
    'data2': np.random.randn(5)
})

#print (df)

grouped1 = df['data1'].groupby(df['key1']).mean()

#print(grouped1)

grouped2 = df['data1'].groupby([df['key1'], df['key2']]).mean()
#print(grouped2)

# Define function
def min_max(arr):
    return arr.max() + arr.min()

# grouped3 = df.groupby('key1')
# grouped3.agg(min_max)
# print(grouped3['data1'].describe())




tips = pd.read_csv('/Users/khuongduy/Documents/KhuongDuy/MCI/GIT/MCI_PY05A10L1/Unit06/tips.csv')
tips['tip_percent'] = tips['tip']*100/ tips['total_bill']
print(tips)

grouped_tips = tips.groupby(['day', 'smoker'])
print(grouped_tips['tip_percent'].agg('mean'))
print(grouped_tips['tip_percent'].agg(['mean', 'std', min_max]))


print(grouped_tips.agg({'tip': np.mean, 'total_bill': 'max'}))

print(grouped_tips.agg({
    'tip_percent':['mean', 'std'],
    'size' : ['median', 'count']
}))

# Apply-Split/ App-Combine
# def top(df, n=5, column='tip_percent'):
#     return df.sort_values(by=column, ascending = False).head(n)

# print(top(tips))

# print(tips.groupby('smoker').apply(top))

# print(tips.groupby('smoker').apply(top, n = 3, column ='total_bill'))

# print(tips.groupby('smoker', group_keys=False).apply(top))

states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon',
          'Nevada', 'California', 'Idaho']
coasts =['East', 'East', 'East', 'East', 'West', 'West', 'West', 'West']
data = pd.Series(np.random.randn(8), index=states)
print(data)
data[::2] = np.nan
print(data)

print(data.fillna(data.mean()))
print(data.groupby(coasts).mean())
print(data.groupby(coasts).apply(lambda x: x.fillna(x.mean())))

# PIVOT TABLE

# Step 1: Tao dataframe
data1 = {
    'Region' : ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product' : ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Sales':[200, 150, 300, 400, 250, 180, 320, 410],
    'Quantity' : [20, 15, 30, 40, 25, 18, 32, 41]
}

df = pd.DataFrame(data1)

# Step 2: Tao bang pivot_table
pivot = pd.pivot_table(
    df, 
    values=['Sales', 'Quantity'],    # Cot can tinh toan
    index= 'Region',                 # Cot lam chi muc
    columns= 'Product',              # Cot phan loai
    aggfunc='sum',                   # ham tinh toan
    fill_value= 0                    # Gia tri mac dinh neu thieu
)


# Step 3: Display pivot table
print("Pivot Table:")
print(pivot)


# grouped = tips.groupby(['day', 'smoker']).mean()
# pivoted = tips.pivot_table(index=['day', 'smoker'])

# TIME-SERIES DATA

# Step 1: Tao DataFrame voi du lieu thoi gian
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = {
    'Date' : date_rng,
    'Sales': np.random.randint(100, 500, size=len(date_rng))    # Random sale data
}

# Step 2: chuyen thanh DataFrame
df3 = pd.DataFrame(data)

# STEP 3: Hien thi
print(df3)

# Chuyen cot 'Date' thanh kieu datetime va dat lam chi muc
df3['Date'] = pd.to_datetime(df3['Date'])
df3.set_index('Date', inplace=True)

# Tao du lieu mau tinh tong doanh so
weekly_sales = df3['Sales'].resample('W').sum()

print('Original Data :')
print(df3)

print("\nWeekly Sales after resample: ")
print(weekly_sales)


# Vi du khac
from datetime import datetime

data_strs = ['2024-09-11 13:40:50', '2024-09-10 00:00:00']
print(pd.to_datetime(data_strs))

idx = pd.to_datetime([*data_strs, None])
print(idx)

print(idx[1])
print(idx[2])
print(pd.isnull(idx))

dates = [datetime(2024, 9, i) for i in range(1,7)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
print(ts.index)

# TIME -SERIES WITH PANDAS
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('2024-09-11', periods=1000))

print(longer_ts)

# select data by year and month
print(longer_ts['2025-09'])

# select data by year
print(longer_ts['2024'])

print(longer_ts.index)
print(longer_ts.index[0])

print(longer_ts['08/03/2025'])
print(longer_ts['20250803'])