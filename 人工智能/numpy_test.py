import numpy as np                  #一般以np作为numpy的别名
a=np.array([2,0,1,5])               #创建数组
print(a)                            #输出数组
print(a[:3])
print(a.min())                      #输出最小值
a.sort()                            #将a的元素排序，此时会直接修改a
b=np.array([[1,2,3],[4,5,6]])       #创建二维数组
print(b*b)                          #输出平方阵
print(b.size)                       #数组元素个数
print(b.shape)                      #数组形状,如b为(2,3)
print(b.ndim)                       #数组维度
print(b.dtype)                      #数组元素类型
#快速创建N维数组的api函数
array_one=np.ones([10,10])          #创建10行10列的数值为浮点1的矩阵
array_zero=np.zeros([5,4])          #创建5行4列的数值为浮点0的矩阵
print(array_one)
print(array_zero)
#数组的正态分布
arr=np.random.normal(1.75,0.1,(4,5))#正态生成4行5列的二维数组
print(arr)
after_arr=arr[1:3,2:4]              #截取第1至2行的第2至3列
print(after_arr)
#改变数组形状
one_20=np.ones([20])                #1行20列
print(one_20)
one_4_5=one_20.reshape([4,5])       #4行5列
print(one_4_5)
#numpy计算
#条件运算
stus_score=np.array([[80,88],[82,81],[84,75],[70,79]])
print(stus_score>80)                #条件判断
print(np.where(stus_score<80,0,90)) #小于80替换为0，大于80替换为90
#统计运算
#指定轴最大值amax(参数1:数组;参数2:axis=0/1;0表示列1表示行)

result=np.amax(stus_score,axis=0)   #每一列的最大值
print(result)

#指定轴最小值amin

result=np.amin(stus_score,axis=0)   #每一列的最小值
print(result)

#指定轴平均值mean

result=np.mean(stus_score,axis=1)   #每一行的平均值
print(result)

#方差

result=np.std(stus_score,axis=1)    #每一行的方差
print(result)

#数组与数的运算

stus_score[:, 0] = stus_score[:, 0]+5 #所有成绩加5分
print("加分后:")
print(stus_score)

stus_score[:, 0] = stus_score[:, 0]*0.5#平时成绩减半
print("减半后:")
print(stus_score)

#矩阵运算

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print("最终结果为:")
print(result)

#矩阵拼接

print("v1为:")
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
print(v1)
print("v2为:")
v2 = [[12, 13, 14, 15, 16, 17], 
      [18, 19, 20, 21, 22, 23]]
print(v2)
# 垂直拼接
result = np.vstack((v1, v2))
print("v1和v2垂直拼接的结果为")
print(result)

# 水平拼接
result = np.hstack((v1, v2))
print("v1和v2水平拼接的结果为")
print(result)
