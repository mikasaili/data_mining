import pandas as pd
import matplotlib.pyplot as plt

# 读取日用电量数据
data = pd.read_csv("D:/courseware/data mining/实验一/第一次实验_数据/User.csv")

# 提取日期和用电量列
date = data["Date"]
usage = data["Eletricity"]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(date, usage, marker='o', linestyle='-')
plt.title("日用电量趋势")
plt.xlabel("Date")
plt.ylabel("Eletricity")
plt.xticks(rotation=45)  # 使日期标签垂直显示
plt.grid(True)
plt.show()

# 读取窃电用户用电数据
user_data = pd.read_csv("D:/courseware/data mining/实验一/第一次实验_数据/Steal user.csv")

# 提取日期和用电量列
user_date = user_data["Date"]
user_usage = user_data["Eletricity"]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(user_date, user_usage, marker='o', linestyle='-')
plt.title("窃电用户用电趋势")
plt.xlabel("Date")
plt.ylabel("Eletricity")
plt.xticks(rotation=45)  # 使日期标签垂直显示
plt.grid(True)
plt.show()