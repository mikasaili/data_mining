import pandas as pd

data = pd.read_excel("D:\\courseware\\data mining\\第三次实验-关联模式实验\\关联模式实验\\data\\menu_orders.xls", header=None)

data_list = data.values.tolist()
data_without_nan = []
for sublist in data_list:
    new_sub = []
    for item in sublist:
        if type(item) == str:
            new_sub.append(item)
        else:
            break
    data_without_nan.append(new_sub)

from FPGrowth import *  # 将上述的所有代码都写在FPGrowth.py文件中

ThresHold = 0.05
model = FPGrowth(ThresHold)
model.fit(data_without_nan)
model.predict()
