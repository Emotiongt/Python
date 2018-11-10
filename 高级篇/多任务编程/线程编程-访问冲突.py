import threading
import time
num=0;
#访问冲突
def f():
    global num
    b=num
    time.sleep(0.0000001)
    num=b+1
    print('%s \n' % threading.currentThread().getName())

def main():
    for i in range(1,20):
        t=threading.Thread(target=f)
        t.setDaemon(True)
        t.start();

    t.join()
    print(num)
if __name__=='__main__':
    main();
