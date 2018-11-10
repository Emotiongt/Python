import threading
import time

def func():
    print(time.ctime())
print(time.ctime())
timer=threading.Timer(1,func)
timer.start()
