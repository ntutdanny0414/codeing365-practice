class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.top#next down#
            self.top = newnode
    def pop(self):
        if self.top is None:
            return 'The Stack is empty'
        else:
            popdata = self.top.data
            self.top = self.top.next
            return 'The data '+ str(popdata) +' is pop'
data = Stack()
outcome = []
while True:
    fun = input().split()
    if fun[0] == '1':
        data.push(int(fun[1]))
    elif fun[0] == '2':
        outcome.append(data.pop())
    elif fun[0] == '3':
        break
for i in range(0,len(outcome)):
    print(outcome[i])
            
