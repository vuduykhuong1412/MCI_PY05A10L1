import pandas as pd

# Loai 1 : Series
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print(s)

data = {'brand': 'toyota', 'color': 'red', 'year':2024, 'speed': '120km/h'}

s2 = pd.Series(data)
print(s2)

s3 = pd.Series(data, index=["brand", "color", "speed"])
print(s3)

# truy cap phan tu Series
print(s2["brand"])
print(s2["color"])

print("----------------")
# truy cap nhieu phan tu
print(s2[['brand','color']])

# truy cap theo dieu kien
print(s2[s2 =='toyota'])

# Loai 1 : Dataframe

data2 = {'Country':['Viet Nam', 'India', 'Brazil'],
         'Capital':['Ha Noi', 'New Delhi', 'Brasilia'],
         'Population':[11190846, 1303171035, 207847528]}

df = pd.DataFrame(data2, columns=['Country', 'Capital', 'Population'])
print(df)

# truy cap phan tu
print(df['Capital'])
print(df[['Capital', 'Country']])

print("------------")
# chon 1 hang trong dataframe
print(df.loc[1])        #1     India  New Delhi  1303171035

# chon nhieu hang
print(df.loc[[1,2]])    #1   India  New Delhi  1303171035
                        #2  Brazil   Brasilia   207847528

# khai bao gia tri trong hang cot
df['Capital'] = 123    # cot
print(df)

# thay doi tren nhieu dong
df['Capital'] = ['Nhat Ban', 'Campuchia', 'Singapore']
print(df)

print('---------------')
print(df.index)