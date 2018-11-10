import threading
import time
lock=threading.RLock()  #创建一个可重入锁
num=0;
def f():
    global num
    #第一次请求锁定
    if lock.acquire():
        print('%s获得可重入锁.\n'%(threading.currentThread().getName()))
        time.sleep(1)
        #第二次请求锁定
        if lock.acquire():
            print('%s获得可重入锁.\n'%(threading.currentThread().getName()))
            time.sleep(1)
            lock.release()  #释放指令锁
            print('%s释放指令锁.\n'%(threading.currentThread().getName()))
        time.sleep(1)
        print('%s释放指令锁.\n'%(threading.currentThread().getName()))
        lock.release()
def main():
    for i in range(1,20):
        t=threading.Thread(target=f)
        t.setDaemon(True)
        t.start();

    t.join()
    print(num)

if __name__=='__main__':
    main();
