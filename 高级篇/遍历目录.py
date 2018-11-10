import os,os.path
#os.walk可以递归完成对当前目录的迭代,输出当前目录下的所有文件(包括子目录下所有文件)
#root返回当前目录,dirs返回当前目录下所有子目录,files返回当前目录下所有文件
def trav_walk(pathname):
    for root,dirs,files in os.walk(pathname):
        for fil in files:
            fname=os.path.abspath(os.path.join(root,fil))
            print(fname)

trav_walk("D:\python txt\pillow")
