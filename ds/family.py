class node:
    def __init__(self, data, up = None):
        self.data = data
        self.up = up
        self.child = []
    def getdata (self):
        return self.data
    def getup (self):
        return self.up
    def setup (self, up):
        self.up = up
    def setchild (self, child):
        self.child.append(child)
    def getchild (self):
        return self.child
    def isroot (self):
        return self.up == None#up#
def nodetoRoot(member, node):
    person = member[node]
    path = [person.getdata()]
    findroot = person
    while not findroot.isroot():
        findroot = findroot.getup()
        path.append(findroot.getdata())
    return path
def nodelen(path1, path2):#need copy#
    a = []
    b = []
    for i in range(0,len(path1)):#copy#
        a.append(path1[i])
    for i in range(0,len(path2)):
        b.append(path2[i])
    for i in range(0,len(a)):
        for j in range(0,len(b)):#len will change#
            if a[i] == b[j]:
                a[i] = ''
                b[j] = ''
    while '' in a:#remove''#
        a.remove('')
    while '' in b:
        b.remove('')
    return len(a) + len(b)
            
member = []
path = []
number = int(input())
for i in range(number):
    member.append(node(i))
for i in range(number - 1):
    relation = [int(e) for e in input().split(' ')]
    member[relation[0]].setchild(member[relation[1]])
    member[relation[1]].setup(member[relation[0]])
for i in range(number):
    path.append(nodetoRoot(member,i))#find i len#
for i in range(0,number-1):#relation#
    for j in range(i+1,number):
        print(str(i)+'-'+str(j)+'-'+str(nodelen(path[i], path[j])))#i and j path save in path#
