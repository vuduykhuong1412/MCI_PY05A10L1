import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# def simulate_price(current_price):
#     data = current_price * np.exp(np.random.normal(size = 1000)* 0.0125).cumprod()
#     return data;


# fig = plt.figure(figsize=(12, 4))
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xticks(list(range(0, 1250, 250)))
# ax.set_title(' Sample data')
# ax.set_xlabel('Step')
# ax.set_ylabel('Price')

# ax.plot(simulate_price(60), 'b-', label='Scenario_1')
# ax.plot(simulate_price(60), 'g-', label='Scenario_2')
# ax.legend(loc= 'best')



# data = pd.Series(simulate_price(60))
# data.plot(figsize=(12, 4))
# plt.show()

# Phan tich data bang seaborn
tips = pd.read_csv('/Users/khuongduy/Documents/KhuongDuy/MCI/GIT/MCI_PY05A10L1/Unit05/tips.csv')


tips['tip_percent'] = tips['tip']* 100 /(tips['total_bill'] - tips['tip'])
sns.barplot(data=tips, x = 'tip_percent', y = 'day', hue = 'time', orient='h')

plt.show()

