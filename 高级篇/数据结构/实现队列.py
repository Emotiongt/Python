class PyQueue:
    #实现队列功能
    def __init__(self,size=20):
        self.queue=[]                  #队
        self.size=size                 #队大小
        self.end=-1                    #队尾
    #设置队大小
    def setSize(self,size):
        self.size=size
    #入队              
    def In(self,element):
        if self.end<self.size-1:
            self.queue.append(element)
            self.end=self.end+1
        else:
            #队满引发异常
            raise QueueException('PyQueueFull')
    #出队
    def Out(self):
        if self.end!=-1:
            element=self.queue[0]
            self.queue=self.queue[1:]
            self.end=self.end-1
            return element
        else:
            #队空引发异常
            raise QueueException('PyQueueEmpty')
    #输出队尾
    def End(self):
        return self.end
    #清除队
    def empty(self):
        self.queue=[]
        self.end=-1
#自定义异常类
class QueueException(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data
if __name__=='__main__':
    queue=PyQueue()
    for i in range(10):
        queue.In(i)
    print(queue.End())
    for i in range(10):
        print(queue.Out())
    for i in range(20):
        queue.In(i)
    queue.empty()
    for i in range(20):
        #此处将引发异常
        print(queue.Out())
