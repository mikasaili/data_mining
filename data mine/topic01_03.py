import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("D:/courseware/data mining/实验一/第一次实验_数据/catering_sale.xls")
# 假设销量低于0或高于某个阈值的数据为异常值
threshold = 10000
filtered_data = data[(data["销量"] > 0) & (data["销量"] <= threshold)]
# 使用describe()方法查看数据的统计量
data_description = filtered_data.describe()
print(data_description)

# 绘制箱线图
p = filtered_data.boxplot(column="销量", return_type='dict')  # 绘制销额的箱线图
x = p['fliers'][0].get_xdata()  # 获取异常值的x坐标
y = p['fliers'][0].get_ydata()  # 获取异常值的y坐标
y.sort()  # 对异常值进行排序

# 添加注释
for i in range(len(x)):
    if i < len(x) - 1:
        plt.annotate(f"{y[i]:.2f}", (x[i], y[i]), xytext=(x[i] + 0.05, y[i] + 1000), fontsize=8,
                     arrowprops=dict(facecolor='red', arrowstyle='->'))
    else:
        plt.annotate(f"{y[i]:.2f}", (x[i], y[i]), xytext=(x[i] - 0.2, y[i] + 1000), fontsize=8,
                     arrowprops=dict(facecolor='red', arrowstyle='->'))

plt.title("餐饮销额数据异常值检测箱线图")
plt.xlabel("销额")
plt.ylabel("销量")
plt.show()

import numpy as np

# 生成示例数据（正弦曲线）
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
error = np.random.rand(10)  # 误差列，可以根据实际数据提供

# 绘制误差棒图
plt.errorbar(x, y, yerr=error, fmt='-o', capsize=4)
plt.title("正弦曲线上的误差棒图")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()