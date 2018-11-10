#实现杨辉三角
def yanghui(n):
    if not str(n).isdecimal() or n<2 or n>25:
        print('杨辉三角参数n必须是不小于2且不大于25的数')
        return False
    x=[]
    for i in range(1,n+1):
        x.append([1]*i)
    for i in range(2,n):
        for j in range(1,i):
            x[i][j]=x[i-1][j]+x[i-1][j-1]
    for i in range(n):
        if n<=10:print(' '*(40-4*i),end='')
        for j in range(i+1):
            print('%-8d' % x[i][j],end='')
        print()

#程序独立运行
if __name__=='__main__':
    print('模块独立运行测试输出')
    print('10阶杨辉三角如下')
    yanghui(10)
