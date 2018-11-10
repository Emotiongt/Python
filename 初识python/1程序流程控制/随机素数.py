#输出10个两位的随机素数
import random
n=0
while n<10:
    x=random.randint(10,99)     #获得一个两位的随机素数
    a=2
    while a<x:
        if x%a==0:break
        a=a+1
    else:
        print(x,end=' ')
        n+=1
