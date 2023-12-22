import pandas as pd
import numpy as np
from scipy.interpolate import lagrange

# 读取Excel文件
data = pd.read_excel("D://courseware//data mining//实验二//data//catering_sale.xls")

# 过滤异常值
data["销量"] = np.where((data["销量"] < 400) | (data["销量"] > 5000), np.nan, data["销量"])

# 定义拉格朗日插值函数
def lagrange_interpolation(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)

# 对空值进行拉格朗日插值
for i in range(len(data)):
    if np.isnan(data.loc[i, "销量"]):
        if i - 5 < 0:
            continue
        data.loc[i, "销量"] = lagrange_interpolation(data["销量"], i)

# 将数据结果保存到文件
data.to_excel("D://courseware//data mining//实验二//data//catering_sale_filtered_interpolated.xlsx", index=False)