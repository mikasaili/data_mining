import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


# 计算欧拉距离
def calcDis(dataSet, centroids, k):
    clalist = []
    for data in dataSet:
        diff = np.tile(data, (k, 1)) - centroids
        squaredDiff = diff ** 2  # 平方
        squaredDist = np.sum(squaredDiff, axis=1)  # 和  (axis=1表示行)
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)
    clalist = np.array(clalist)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    return clalist


# 计算质心
def classify(dataSet, centroids, k):
    # 计算样本到质心的距离
    clalist = calcDis(dataSet, centroids, k)
    # 分组并计算新的质心
    minDistIndices = np.argmin(clalist, axis=1)  # axis=1 表示求出每行的最小值的下标
    newCentroids = pd.DataFrame(dataSet).groupby(minDistIndices).mean()
    newCentroids = newCentroids.values

    # 计算变化量
    changed = newCentroids - centroids

    return changed, newCentroids


# 使用k-means分类
def kmeans(dataSet, k):
    # 随机取质心
    centroids = random.sample(dataSet, k)

    # 更新质心 直到变化量全为0
    changed, newCentroids = classify(dataSet, centroids, k)
    while np.any(changed != 0):
        changed, newCentroids = classify(dataSet, newCentroids, k)

    centroids = sorted(newCentroids.tolist())  # tolist()将矩阵转换成列表 sorted()排序

    # 根据质心计算每个集群
    cluster = []
    clalist = calcDis(dataSet, centroids, k)  # 调用欧拉距离
    minDistIndices = np.argmin(clalist, axis=1)
    for i in range(k):
        cluster.append([])
    for i, j in enumerate(minDistIndices):  # enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])

    return centroids, cluster


if __name__ == '__main__':
    # 读取 Excel 数据
    file_path = 'D:\\courseware\\data mining\\第三次实验\\data\\consumption_data.xls'
    data = pd.read_excel(file_path, header=0)
    da = pd.DataFrame(data)
    da = da[['R', 'F', 'M']]

    # 数据归一化处理
    da_scaled = StandardScaler().fit_transform(da)

    dataset = da_scaled.tolist()
    centroids, cluster = kmeans(dataset, 3)
    for i in range(len(centroids)):
        print('质心为：%s' % centroids[i])
    for i in range(len(cluster)):
        print('集群为：%s' % cluster[i])
        print("总数为:", len(cluster[i]))
    for i in range(len(dataset)):
        plt.scatter(dataset[i][0], dataset[i][1], marker='o', color='green', s=40, label='原始点')
        #  记号形状       颜色      点的大小      设置标签
    for j in range(len(centroids)):
        plt.scatter(centroids[j][0], centroids[j][1], marker='x', color='red', s=50, label='质心')
    plt.show()
