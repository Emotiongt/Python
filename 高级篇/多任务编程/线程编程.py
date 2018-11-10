import threading

#线程编程
def f(i):
    print(' I am from a thread,num=%d\n' % (i))
def main():
    for i in range(1,10):
        t=threading.Thread(target=f,args=(i,))
        #设置是否为守护线程
        t.setDaemon(True)
        t.start();

if __name__=='__main__':
    main()
