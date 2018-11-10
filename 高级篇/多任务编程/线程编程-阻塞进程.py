import threading

#线程编程-阻塞进程
def f(i):
    print(' I am from a thread,num=%d\n' % (i))
def main():
    for i in range(1,10):
        t=threading.Thread(target=f,args=(i,))
        t.setDaemon(True)
        t.start();
    #阻塞进程
    t.join()

if __name__=='__main__':
    main()
