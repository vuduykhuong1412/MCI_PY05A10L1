# Bai 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/khuongduy/Documents/KhuongDuy/MCI/GIT/MCI_PY05A10L1/Unit05/sales_data.csv")
# profitList = df['total_profit'].to_list()
# monthList = df['month_number'].to_list()
# plt.plot(monthList, profitList, label = "Loựi nhuận các tháng trong năm")
# plt.xlabel('Số tháng')
# plt.ylabel("Lợi nhuận bằng Dollar")
# plt.xticks(monthList)
# plt.title('Lợi nhuận công ty theo tháng')
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.show()

# Bai 5
monthList = df['month_number'].tolist()
faceCreamSaleData = df['facecream'].tolist()
faceWashSaleData = df['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCreamSaleData, width=0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSaleData, width=-0.25, label='Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.title('Sales data')
plt.legend(loc='upper left')

plt.xticks(monthList)
plt.grid(True, linewidth = 1, linestyle='--')
plt.show()