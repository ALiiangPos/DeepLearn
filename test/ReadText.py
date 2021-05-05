import pandas as pd
import numpy as np 
from io import BytesIO
import math 
df_1 = pd.read_excel("D:\BaiduNetdiskDownload\hello\.vscode\数据\附件1.xlsx" , header=0)

industry_table = []

'''
找到制造业股票代码
'''
for text in df_1.index :
    text=df_1.loc[text]
    if(text['所属行业'] == '制造业'):
        industry_table.append(int(text['股票代码']))
        
'''
找到所有制造业的数据  并初始化 
'''
df_2 = pd.read_csv("D:\BaiduNetdiskDownload\hello\.vscode\数据\附件2(样例数据).csv" , header=0 ,index_col = 0) 
manufactureTable = []
for i in df_2.index :
    if i in industry_table :
        manufactureTable.append(df_2.loc[i]) 
for text in manufactureTable :
    # print(text['END_DATE'])
    for i in range(len(text)):
        if type(text[i]) == type('A'):
            continue
        if math.isnan( float(text[i]) ) :
            text[i] = 0
with open ("data.csv" , 'w') as f :
    for text   in manufactureTable :
        for i in range(len(text)):
            f.write( str(text[i]) ) 
            f.write("  ")
        f.write('\n')
