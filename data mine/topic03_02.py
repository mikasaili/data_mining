import subprocess
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import os

os.environ["PATH"] += os.pathsep + 'D:\\software\\Graphviz\\bin'
# 读取 Excel 数据
file_path = 'D:\\courseware\\data mining\\第三次实验\\data\\sales_data.xls'
data = pd.read_excel(file_path)

# 提取特征列和标签列
feature_columns = data.columns[1:4]
class_column = data.columns[4]

# 选择第2、3、4列作为样本特征，第5列作为样本类别
x = data[feature_columns]
y = data[class_column]

# 将类别标签转换为数值数据
y = y.map({'好': 1, '是': 1, '高': 1, '坏': -1, '否': -1, '低': -1})
x = x.applymap({'是': 1, '否': -1, '好': 1, '坏': -1, '高': 1, '低': -1}.get)

model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(x, y)

# 将决策树模型可视化为 DOT 文件
dot_file_path = 'D:\\courseware\\data mining\\第三次实验\\data\\decision_tree.dot'
export_graphviz(model, out_file=dot_file_path, feature_names=feature_columns, class_names=['-1', '1'], filled=True,
                rounded=True, impurity=True)

# 将 DOT 文件转换为 PDF（或其他格式）
output_image_path = 'D:\\courseware\\data mining\\第三次实验\\data\\decision_tree.png'
subprocess.run(['dot', '-Tpng', '-Nfontname=simsun', '-Efontname=simsun', dot_file_path, '-o', output_image_path])
