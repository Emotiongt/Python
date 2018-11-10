import threading
import time
#事件对象e(初始值为false)
#set()：将内置标记设置为true
#clear(): 将内置标记设置为false
#wait(): 阻塞进程至事件对象的内置标记被设置为True
e=threading.Event()       #创建一个事件对象e
def f1():
    print('%s start.\n' % (threading.currentThread().getName()))
    time.sleep(5)
    print('触发事件.\n')
    e.set()

def f2():
    e.wait();
    print('%s start.\n' % (threading.currentThread().getName()))

def main():
    t1=threading.Thread(target=f1)
    t1.setDaemon(True)
    t1.start();
    t2=threading.Thread(target=f2)
    t2.setDaemon(True)
    t2.start();

if __name__=='__main__':
    main();
    
