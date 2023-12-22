import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 读取excel数据
file_path = 'D:\\courseware\\data mining\\第三次实验\\data\\bankloan.xls'
data = pd.read_excel(file_path)  #读取数据

# 将前8列数据作为样本特征(x)，第9列数据作为样本类别(y)
X = data.iloc[:, :8]
y = data.iloc[:, 8]

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.70, random_state=40)

# 3. 训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. 预测并计算准确率
y_pred_train = model.predict(X_train)
accuracy_train = accuracy_score(y_train, y_pred_train)

print(f"逻辑回归在训练数据上的平均准确率: {accuracy_train:.8f}")