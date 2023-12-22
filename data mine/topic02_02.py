import pandas as pd

# 读取Excel文件
data = pd.read_excel("D://courseware//data mining//实验二//data//normalization_data.xls",header=None)

# 1. 最小-最大规范化（Min-Max Normalization）
min_max_scaler = (data-data.min())/(data.max()-data.min())

# 2. 零-均值规范化（Z-score Normalization）
z_score_scaler = (data-data.mean()) / data.std()

# 3. 小数定标规范化（Decimal Scaling Normalization）
decimal_scaler = lambda x: x / 10**len(str(abs(x.max())))
data_decimal_scaled = data.apply(decimal_scaler)

# 打印规范化后的数据
print("最小-最大规范化后的数据：")
print(min_max_scaler)

print("\n零-均值规范化后的数据：")
print(z_score_scaler)

print("\n小数定标规范化后的数据：")
print(data_decimal_scaled)
