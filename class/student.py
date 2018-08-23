class student(object):
    def __init__(self,index, stuid, score):
        self.stuid = stuid
        self.score = score
        self.index = index
        self.next = None
class Class:
    def __init__(self,index = None,stuid=None, score=None):
        if index is None and stuid is None and score is None:
            self._Head = None
        else:
            self._Head = student(index,stuid, score)
#        self._Tail = self._Head
    def size(self):
        student1 = self._Head
        size = 0
        while student1 is not None:
            size = size + 1
            student1 = student1.next#need next!!!#
        return size
    def getindex(self,index):
        student1 = self._Head
        while student1.index != index:
            student1 = student1.next
        return student1
    def reindex(self):
        student1 = self._Head
        for i in range(1,self.size()+1):
            student1.index = i
            student1 = student1.next
    def findindex(self, stuid, score):
        if self._Head is None:
            return [1,0]
#            self._Tail = newstudent
        else:
            sort = []
            findstudent = self._Head
            while findstudent is not None:
                sort.append([findstudent.score,findstudent.stuid])
                findstudent = findstudent.next
            sort.append([score,stuid])
            sort = sorted(sort)
            findindex = sort.index([score,stuid])+1
            if findindex == len(sort):
                compare = findindex-1
            else:
                compare = findindex
            return [findindex,compare]
    def append(self,index,stuid, score):#index is [0]#
        student1 = student(index,stuid, score)
        outcome = 'Insert data '+str(stuid)+':'+str(score)+', compare:'+str(self.findindex(stuid, score)[1])+'.'
        if self._Head is None:
            self._Head = student1
            self.reindex()
        elif index == 1:
            student1.next = self._Head
            self._Head = student1
            self.reindex()
        elif index == self.size() + 1:
            studentindex = self.getindex(self.size())
            studentindex.next = student1
            self.reindex()
        else:
            studentindex = self.getindex(index - 1)
            student1.next = studentindex.next
            studentindex.next = student1
            self.reindex()
        print(outcome)
    def findstudent(self,stuid):
        findstudent = self._Head
        while findstudent is not None:
            if findstudent.stuid == stuid:
                break
            else:
                findstudent = findstudent.next
        if findstudent is not None:
            return findstudent
        else:
            return None
    def delete(self,stuid):#after delete reindex#
        deletestudent = self.findstudent(stuid)
        if deletestudent == None:
            print('Student '+str(stuid)+' is not exist.')
        else:
            if deletestudent.index == 1:
                first = self.getindex(1)
#                second = self.getindex(2)
#                first.next = None
                self._Head = first.next
                self.reindex()
            elif  deletestudent.index == self.size():
                pre = self.getindex(deletestudent.index-1)
                pre.next = None
                self.reindex()
            else:
                pre = self.getindex(deletestudent.index-1)
                pre.next = deletestudent.next
                deletestudent.next = None
                self.reindex()
            print('Delete student '+str(stuid)+' successful.')
    def printdata(self):
        printdata = []
        student1 = self._Head
        if student1 == None:
            print('null')
        else:    
            while student1 is not None:
                printdata.append(str(student1.stuid)+':'+str(student1.score))
                student1 = student1.next#need to next#
            print(','.join(printdata))
quene = Class()
while True:
    need = input().rstrip(' ')
    if need == 'p':
        quene.printdata()
    elif need == 'i':
        data = input().split(',')
        data[0] = int(data[0])#not == !!#
        data[1] = int(data[1])#use.[0]#
        quene.append(quene.findindex(data[0],data[1])[0],data[0],data[1])
    elif need == 'd':
        data = int(input())
        quene.delete(data)
    elif need == 'e':
        break
