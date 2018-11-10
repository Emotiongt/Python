class PyStack:
    #堆栈数据结构
    def __init__(self,size=20):
        self.stack=[]
        self.size=size
        self.top=-1               #栈顶位置
    #设置堆栈大小
    def setSize(self,size):       
        self.size=size
    #元素进栈
    def push(self,element):
        if self.isFull():
            raise StackException('PyStackOverflow')   #栈满引发异常
        else:
            self.stack.append(element)
            self.top=self.top+1
    #元素出栈
    def pop(self):
        if self.isEmpty():
            raise StackException('PyStackUnderflow')  #栈空引发异常
        else:
            element=self.stack[-1]
            self.top=self.top-1
            del self.stack[-1]
            return element
    #获取栈顶位置
    def Top(self):
        return self.top
    #清空栈
    def empty(self):
        self.stack=[]
        self.top=-1
    #是否为空栈
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    #是否为满栈
    def isFull(self):
        if self.top==self.size-1:
            return True
        else:
            return False

class StackException(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data

if __name__=='__main__':
    stack=PyStack()
    for i in range(10):
        stack.push(i)
    print(stack.Top())
    for i in range(10):
        print(stack.pop())
    stack.empty()
    #此处将引发异常
    for i in range(21):
        stack.push(i)
    
