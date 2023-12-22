import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("D:/courseware/data mining/实验一/第一次实验_数据/catering_fish_congee.xls",header=None, names=["日期", "销售额"])
# 设置组距和计算组数
bin_width = 500  # 组距
min_value = int(data["销售额"].min() // bin_width * bin_width)  # 最小值取整
max_value = int(data["销售额"].max() // bin_width * bin_width) + bin_width  # 最大值取整并加上组距
num_bins = int((max_value - min_value) / bin_width)  # 计算组数

plt.hist(data["销售额"], bins=num_bins, range=(min_value, max_value), color='skyblue', edgecolor='black')
plt.xlabel("sales")
plt.ylabel("fre")
plt.title("histigram")
plt.show()
