import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x0' : [1, 2, 3, 4, 5],
    'x1' : [0.01, -0.01, 0.25, -4.1, 0.],
    'y':[-1.5, 0.0, 3.6, 1.3, -2.0]
})

print(data)
print(data.columns)

df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
print(df2)

df3 = data.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
print(df3)

model_cols = ['x0', 'x1']
print(data.loc[:, model_cols].values)
print(data[model_cols].values)


data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'],
                                  categories=['a', 'b'])

print(data)

dummies = pd.get_dummies(data.category, prefix='category')
print(dummies)

data_with_dummies = data.drop('category', axis=1).join(dummies)
print(data_with_dummies)

#CREATING MODEL DESCRIPTIONS WITH PATSY

import patsy


y, X = patsy.dmatrices('y ~ x0 + x1', data)

print(X)
print(y)

print(np.asarray(X))
print(patsy.dmatrices('y ~ x0 + x1 + 0', data)[1])

print(np.linalg.lstsq(X, y))

coef, resid, _, _ = np.linalg.lstsq(X, y)
print(coef)
print(coef.squeeze())

y1, X1 = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)
print(X1)

y2, X2 = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)
print(X2)

# Vi du patsy.center(x)
x = [ 1, 2, 3, 4, 5]

x_center = patsy.center(x)
print(x_center)

#==> patsy.center(x) : trừ giá trị trung bình dữ liệu xoay quanh 0

# vi du patsy.standardize(x)
x_standardize = patsy.standardize(x)
print(x_standardize)

#==> pasty.standardizes(x) : Chuẩn hoá dữ liệu với trung bình 0 và độ lệch chuẩn chuẩn 1