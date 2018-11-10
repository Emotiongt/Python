#输出数字金字塔
for x in range(1,10):
    print(' '*(15-x),end='')        #输出每行前的空格
    n=x                             #print()默认打印一行,end=''表示末尾不换行,加空格
    while n>=1:
        print(n,sep='',end='')      #输出前半部分数据
        n-=1                        #sep=''表示分隔符为''
    n+=2
    while n<=x:
        print(n,sep='',end='')
        n+=1
    print()
