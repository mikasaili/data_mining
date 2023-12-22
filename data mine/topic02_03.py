import pandas as pd
from sklearn.decomposition import PCA

# 读取Excel文件
data = pd.read_excel("D://courseware//data mining//实验二//data//principal_component.xls",header=None)

# 创建PCA模型
pca = PCA()

# 拟合模型
pca.fit(data)

# 查看模型的各个特征向量
components = pca.components_
print("模型的特征向量（主成分）：")
print(components)

# 查看模型的各个成分各自的方差百分比
explained_variance_ratio = pca.explained_variance_ratio_
print("\n每个成分的方差百分比：")
print(explained_variance_ratio)