class node:
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.right = None
        self.left = None
    def getRightChild(self):
        return self.right
    def getLeftChild(self):
        return self.left
    def getnumber(self):
        return self.number
    def setParent(self, p):
        self.parent=p
    def addRightChild(self, hnode):
        self.right=hnode
        hnode.setParent(self)
    def addLeftChild(self, hnode):
        self.left=hnode
        hnode.setParent(self)
    def hasRightChild(self):#print need#
        return (self.right!=None)
    def hasLeftChild(self):
        return (self.left!=None)
class BST:
    def __init__(self):
        self.root=None
        self.size=0
    def isEmpty(self):
        return (self.size==0)
    def add(self,key):
        if self.isEmpty():
            self.root = node(key)
            self.size = self.size+1#size+1#
        else:
            start = self.root
            while True:
                if start.getnumber() >= key:#>=#
                    if start.getLeftChild() == None:
                        start.addLeftChild(node(key))
                        break
                    else:
                        start = start.getLeftChild()
                else:
                    if start.getRightChild() == None:
                        start.addRightChild(node(key))
                        break
                    else:
                        start = start.getRightChild()
            self.size = self.size+1
    def inorder(self,start):#start = root node#node need recursion
        if start==None:#mean no root#
            print('null',end = '')#also end#
        else:
            if start.hasLeftChild():
                self.inorder(start.getLeftChild())
            print(start.getnumber(),end = ' ')#end + \n#
            if start.hasRightChild():#list also cant#
                self.inorder(start.getRightChild())
tree = BST()
while True:
    want = input()
    if want == 'e':
        break
    elif want == 'p':
        tree.inorder(tree.root)#start root#
        print()#\n#
    elif want == 'i':
        addnum = int(input())
        tree.add(addnum)
