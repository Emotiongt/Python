#Python实现链表
class Node():
    #实现节点
    __slots__=['_item','_next']
    def __init__(self,item):
        self._item=item
        self._next=None
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item=newitem
    def setNext(self,newnext):
        self._next=newnext
class SingleLinkedList():
    #初始化链表为空表
    def __init__(self):
        self._head=None
        self._size=0
    #检测是否为空
    def isEmpty(self):
        return self._head==None
    #在链表前端添加元素
    def add(self,item):
        temp=Node(item)
        temp.setNext(self._head)
        self._head=temp
    #在链表尾部添加元素
    def append(self,item):
        temp=Node(item)
        if self.isEmpty():
            self._head=temp
        else:
            current=self._head
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
    #返回元素在链表中的位置
    def index(self,item):
        current=self._head
        count=0
        found=None
        while current!=None and not found:
            count+=1
            if current.getItem()==item:
                found=True
            else:
                current=current.getNext()
        if found:
            return count
        else:
            print('not found')
    #删除链表指定元素
    def remove(self,item):
        current=self._head
        pre=None
        while current!=None:
            if current.getItem()==item:
                if not pre:
                    self._head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre=current
                current=current.getNext()
    #在链表中插入元素
    def insert(self,pos,item):
        if pos<=1:
            self.add(item)
        elif pos>self.size():
            self.append(item)
        else:
            temp=Node(item)
            count=1
            pre=None
            current=self._head
            while count<pos:
                count+=1
                pre=current
                current=current.getNext()
            pre.setNext(temp)
            temp.setNext(current)
if __name__=='__main__':
    a=SingleLinkedList()
    for i in range(1,10):
        a.append(i)
    print(a.size())
    a.travel()
    print(a.index(5))
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()
