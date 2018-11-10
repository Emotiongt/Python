import threading
import time
s=threading.Semaphore(2)    #创建一个计数器初值为2的信号量对象s
num=0;
def f():
    global num
    #第一次请求锁定
    if s.acquire():
        print('%s获得信号量.\n'%(threading.currentThread().getName()))
        time.sleep(1)
        print('%s释放信号量.\n'%(threading.currentThread().getName()))
        s.release()

def main():
    for i in range(1,10):
        t=threading.Thread(target=f)
        t.setDaemon(True)
        t.start();

    t.join()

if __name__=='__main__':
    main()
