import numpy as np
import pandas as pd

# data = pd.DataFrame(np.random.randint(1, 10, size=(6, 9)),
#     index=[['A', 'B', 'B', 'C', 'C', 'C'],[1, 2, 3, 4, 5, 6]],
#     columns=[['I', 'I', 'II', 'II', 'II','II', 'III', 'III', 'III'],[1, 2, 1, 2, 3, 4, 1, 2, 3]])
# print(data)

# print(data.index)

# # TRUY CAP DUA VAO SO COT
# print(data['II'])
# print("===")
# print(data['III'])
# # ==> truy cap thong qua cot 

# print("++++++")
# print(data.loc[:, 'I': 'II'])

# # ==> truy cap su dung loc[so_hang, so_cot]

# print("_____")
# print(data.loc[:, ['I', 'III']])
# #==> truy cap so cot duoc chon

# print('Truy cap dua vao level column\n')
# print(data['II'][3])

# # ==> truy cap cot II tinh tu hang thu 3
# # data[so_cot][tu_hang_so_n]

# # TRUY CAP DUA VAO SO HANG
# print('--truy cap dua vao so hang\n')
# print(data.loc['B', :])

# print(data.loc['B':'C', :])

# print(data.loc[['A', 'C'], :])

# print(data.loc['B', :].loc[2,:])

# print('Gan index name\n')
# data.index.names = ['one', 'two']
# print(data)
# data.columns.names = ['first', 'second']
# print(data)

# print("==============================\n")
# df1 = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
#                     'A':['A0', 'A1', 'A2', 'A3'],
#                     'B':['B0', 'B1', 'B2', 'B3']
#                     })

# print(df1)

# df2 = pd.DataFrame({
#     'key':['K0', 'K1', 'K1', 'K4'],
#     'C':['C0', 'C1', 'C2', 'C3'],
#     'D':['D0', 'D1', 'D2', 'D3']

# })
# print(df2)

# # inner join
# df1_inner_df2 = pd.merge(df1, df2, on='key')
# print(df1_inner_df2)

# # left join
# df1_left_df2 = pd.merge(df1, df2, on='key', how='left')
# print(df1_left_df2)

# # right join
# df1_right_df2 = pd.merge(df1, df2, on='key', how='right')
# print(df1_right_df2)

# # full join
# df1_full_df2 = pd.merge(df1, df2, on='key', how='outer')
# print(df1_full_df2)
# print("++++++++++++++++++\n")

# # concat ==> hop 2 matrix theo cot
# df1_concat_df2 = pd.concat([df1, df2])
# print(df1_concat_df2)

# # concat ==> hop 2 matrix theo hang
# df1_concat_h_df2 = pd.concat([df1, df2], axis=1)
# print(df1_concat_h_df2)


# RESHAPING DATA
data = pd.DataFrame(np.random.randint(1, 10, size=(6, 9)),
    index=[['A', 'B', 'B', 'C', 'C', 'C'],[1, 2, 3, 4, 5, 6]],
    columns=[['I', 'I', 'II', 'II', 'II','II', 'III', 'III', 'III'],[1, 2, 1, 2, 3, 4, 1, 2, 3]])
print(data)

# slice1 = data.loc[idx[:'B'], 'II']
# print(slice1)

# PIVOTING
# df = pd.DataFrame({
#     'foo':['one', 'one', 'one', 'two', 'two', 'two'],
#     'bar':['A', 'B', 'C', 'A', 'B', 'C'],
#     'baz': [1, 2, 3, 4, 5, 6],
#     'zoo':['x', 'y', 'z', 'q', 'w', 't']

# })
# print(df)

# df_pivot = df.pivot(index='foo', columns='bar', values='baz')
# print(df_pivot)

# df = pd.read_csv('MCI_PY05A10L1/Unit05/macrodata.csv')
# print(df)

# columns = pd.Index(['realgdp', 'infl', 'unemp'], name = 'stat')
# print(columns)

# new_data = df.reindex(columns=columns)
# print(new_data)

# periods = pd.PeriodIndex(year = df.year, quarter = df.quarter, name = 'date')
# print(periods)

# print(periods.end_time)

# new_data.index = periods.end_time
# print(new_data)

# print(new_data.stack())
# print(new_data.stack().reset_index())

# # rename dataFrame coulmns

# stacked = new_data.stack().reset_index().rename(columns={0:'value'})
# print(stacked)


# VISUALIZATION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = np.sin(np.arange(0, 2 * math.pi, 0.1)**2)

# ve
#fig = plt.plot(data)
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

# ax1.plot(np.arange(0.0, 5.0, 0.2),'r--')
# ax2.plot(np.random.randn(50).cumsum(), 'k--')
# ax3.plot(np.sin(np.arange(0.3*np.pi, 0.1)))
# plt.show()

# fig, axes = plt.subplots(2, 2, sharex = True, sharey = True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(50), bins = 50, color='g', alpha= 0.5)

# plt.subplots_adjust(wspace=1, hspace=1)
# plt.show()

# TICKS, LABELS, LEGENDS
x = np.arange(0, 2*math.pi, 0.05)
y = np.sin(x)

axes = plt.axes()
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.title('Biểu diễn đồ thị hình sin')

plt.plot(x, y, color='b')

# set grid
plt.grid(True, linewidth =1, linestyle="--")

# setting ticker for x,y
axes.set_xticks([0, 2, 4, 6])
axes.set_yticks([-1, 0, 1])

# set label for y ticks
axes.set_yticklabels(["sin(-90)", "sin(0)", "sin(90)"])

# save File image
plt.savefig("/Users/khuongduy/Documents/KhuongDuy/MCI/GIT/MCI_PY05A10L1/Unit05/sinFigure.png", dpi=150)
plt.show()
