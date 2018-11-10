import threading
import time
lock=threading.Lock()
num=0;
#指令锁
def f():
    global num
    #获得指令锁
    if lock.acquire():
        print('%s获得指令锁 \n' % threading.currentThread().getName())
    b=num
    time.sleep(0.0000001)
    num=b+1
    #释放指令锁
    lock.release()
    print('%s释放指令锁 \n' % threading.currentThread().getName())

def main():
    for i in range(1,20):
        t=threading.Thread(target=f)
        t.setDaemon(True)
        t.start();

    t.join()
    print(num)
if __name__=='__main__':
    main();
