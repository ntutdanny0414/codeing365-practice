class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next = next
class Queue:
    def __init__(self,name):
        self.head = None
        self.name = name
    def getname(self):
        return self.name
    def getsize(self):
        nodeh = self.head
        size = 0
        while nodeh is not None:
            size = size + 1
            nodeh = nodeh.next
        return size
    def enqueue(self,data):
        new_node = Node(data)
        first = self.head
        if first is None:
            self.head = new_node
        else:
            while first.next is not None:
                first = first.next
            first.setnext(new_node)
    def dequeue(self):
        first = self.head
        if first != None:
            self.head = first.next
            first.setnext(None)
        else:
            print("Queue is empty")
    def MergeQueue(self,queneb):
        first = self.head
        if first is None:
            self.head = queneb.head
        else:
            while first.next is not None:
                first = first.next
            first.setnext(queneb.head)
        queneb.head = None
        queneb.name = None
    def PrintAllQueue(self):
        first = self.head
        if first is None:
            print('Queue Name:'+str(self.getname())+' Queue Size:'+str(self.getsize())+' Queue Element:Queue is empty')
        else:
            alldata = []
            while first is not None:
                alldata.append(str(first.getdata()))
                first = first.next
            print('Queue Name:'+str(self.getname())+' Queue Size:'+str(self.getsize())+' Queue Element:'+' '.join(alldata))
alldata = {}
while True:
    fun = int(input())
    if fun == 1:
        name = input()
        data = Queue(name)
        alldata[str(data.getname())] = data
    elif fun == 2:
        name = input().rstrip(' ')
        if name not in alldata:
            print('Queue '+name+' isn\'t exist')
        else:
            sdata = int(input())
            alldata[name].enqueue(sdata)#SDATA!!#
    elif fun == 3:
        name = input().rstrip(' ')
        if name not in alldata:
            print('Queue '+name+' isn\'t exist')
        else:
            alldata[name].dequeue()
    elif fun == 4:
        namea = input()
        nameb = input()
        if namea not in alldata or nameb not in alldata:
            if namea not in alldata:
                print('Queue '+namea+' isn\'t exist')
            if nameb not in alldata:
                print('Queue '+nameb+' isn\'t exist')
        else:
            alldata[namea].MergeQueue(alldata[nameb])
            del alldata[nameb]
    elif fun == 5:
        if len(alldata) == 0:
            print('****************************************')
            print('Isn\'t have any queue')
            print('****************************************')
        else:
            print('****************************************')
            for i in alldata:
                alldata[i].PrintAllQueue()#no need print#
            print('****************************************')
    elif fun == 6:
        break
            
            
