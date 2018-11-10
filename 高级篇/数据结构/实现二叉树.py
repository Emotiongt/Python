class BTree:
    #Python实现二叉树
    def __init__(self,value):
        self.left=None                #左子树
        self.data=value               #节点值
        self.right=None               #右子树
    #向左子树插入节点
    def insertLeft(self,value):
        self.left=BTree(value)
        return self.left
    #向右子树插入节点
    def insertRight(self,value):
        self.right=BTree(value)
        return self.right
    #输出节点数据
    def show(self):
        print(self.data)
def preorder(node):
    #先序遍历
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)
def inorder(node):
    #中序遍历
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)
def postorder(node):
    #后序遍历
    if node.data:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        node.show()
if __name__=='__main__':
    Root=BTree('Root')
    A=Root.insertLeft('A')
    C=A.insertRight('C')
    D=A.insertRight('D')
    F=D.insertLeft('F')
    G=D.insertRight('G')
    B=Root.insertRight('B')
    E=B.insertRight('E')
    print('*************************')
    print('Binary Tree Pre-Traversal')
    print('*************************')
    preorder(Root)
    print('*************************')
    print('Binary Tree Pre-Traversal')
    print('*************************')
    inorder(Root)
    print('*************************')
    print('Binary Tree Pre-Traversal')
    print('*************************')
    postorder(Root)
