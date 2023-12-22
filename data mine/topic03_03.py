from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # 读取 Excel 数据
    file_path = 'D:\\courseware\\data mining\\第三次实验\\data\\consumption_data.xls'
    data = pd.read_excel(file_path, header=0)
    da = pd.DataFrame(data)
    da = da[['R', 'F', 'M']]

    # 数据归一化处理
    da_scaled = StandardScaler().fit_transform(da)

    # 定义 K-Means 模型
    kmeans = KMeans(n_clusters=3, max_iter=30, n_init=10)

    # 进行聚类
    da['聚类类别'] = kmeans.fit_predict(da_scaled)
    data['聚类类别'] = da['聚类类别']

    # 打印聚类中心和各类别的样本数
    print("聚类中心:")
    print(kmeans.cluster_centers_)
    print("\n各类别的样本数:")
    print(da['聚类类别'].value_counts())

    # 将结果添加到原始 Excel 文件中
    data.to_excel(file_path, index=False, engine='openpyxl')

    # 输出各类别的特征概率密度函数
    sns.set(style="whitegrid")

    for cluster in range(3):
        plt.figure(figsize=(8, 5))
        for i, feature in enumerate(['R', 'F', 'M']):
            plt.subplot(3, 1, i + 1)
            sns.kdeplot(da[da['聚类类别'] == cluster][feature], label=f'Cluster {cluster}', color=f'C{cluster}')

            plt.title(f'Distribution of {feature} in Cluster {cluster}')
            plt.xlabel(feature)
            plt.ylabel('Density')
            plt.legend()

        plt.tight_layout()
        plt.show()
