import pandas as pd
import numpy as np 
from io import BytesIO
df_1 = pd.read_excel("D:\浏览器下载\泰迪杯数据\附件1.xlsx" , header=0)

industry_table = []

for text in df_1.index :
    text=df_1.loc[text]
    if(text['所属行业'] == '制造业'):
        industry_table.append(int(text['股票代码']))

df_2 = pd.read_csv("D:\浏览器下载\泰迪杯数据\\analyze.csv" , header=0 ,index_col = 0) 
manufactureTable = []
for i in df_2.index :
    if i in industry_table :
        manufactureTable.append(df_2.loc[i]) 
for text   in manufactureTable :
    print(text['END_DATE'])
# list = [1 ,2,3,5,8]x
# ad = np.array(list)
# for i in ad : 
#     print(i)


# # encode str→bytes bytes→str decode
# data = BytesIO("1 2 3\n 4 5 6".encode())
# text = np.genfromtxt(data, names="A, B, C")
# # 输出 A属性 列
# print(text['A'])
# # 输出第 1 行 
# print(text[0])

# np.array(shape ,ndim , dtype)