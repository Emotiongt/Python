import pandas as pd
s=pd.Series([1,2,3],index=['a','b','c'])               #创建一个序列s
d=pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c']) #创建一个表
d2=pd.DataFrame(s)                                     #使用已有序列创建表

print(d.head())                                        #预览前5行数据
print(d.describe())                                    #数据基本统计量
d.to_csv('data.csv')
pd.read_csv('data.csv',encoding='utf-8')
