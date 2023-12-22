import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("D:/courseware/data mining/实验一/第一次实验_数据/catering_dish_profit.xls")
print(data.describe())

# 计算不同菜品的销售总量
dish_sales = data.groupby("菜品名")["盈利"].sum()

# 饼图
plt.figure(figsize=(8, 8))
plt.pie(dish_sales, labels=dish_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Different dish profit-pie")
plt.axis("equal")  # 保持图形圆形
plt.show()

# 条形图
plt.figure(figsize=(10, 6))
plt.bar(dish_sales.index, dish_sales)
plt.xlabel("菜品名")
plt.ylabel("盈利")
plt.title("Different dish profit-bar chart")
plt.xticks(rotation=90)  # 使x轴标签垂直显示
plt.show()

