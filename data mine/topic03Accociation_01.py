import pandas as pd
import Apriori
file_path = "D:\\courseware\\data mining\\第三次实验-关联模式实验\\关联模式实验\\data\\menu_orders.xls"
data = pd.read_excel(file_path,header=None)
ct = lambda x: pd.Series(1, index=x[pd.notna(x)])
b = map(ct, data.values)
data_01matrix = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，NAN用0填充
print(Apriori.item(data_01matrix))
