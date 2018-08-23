class university:
    def __init__(self,name):
        self.name = name
        self.attribute = []
    def getattribute(self):
        return self.attribute
    def getname(self):
        return self.name
    def append(self,attri):
        self.attribute.append(attri)
    def hasattri(self,attri):
        return attri in self.attribute
def doandlist(wantto,allschool):
    andlist = []
    for j in range(0,len(wantto),2):
        hasschool = []
        for i in range(0,len(allschool)):
            if allschool[i].hasattri(wantto[j]+wantto[j+1]):
                hasschool.append(allschool[i].getname())##school
        andlist.append(hasschool)
    schoolset = set(andlist[0])#init#
    for i in range(1,len(andlist)):
        schoolset = schoolset & set(andlist[i])#set([i])#
    return schoolset
data = int(input())
allschool = []
for j in range(data):
    school = input().split(' ')
    aschool = university(school[0])
    for i in range(1,len(school)):#ij#
        aschool.append(school[i])
    allschool.append(aschool)
want = int(input())
for i in range(want):
    orlist = []
    wantto = input().replace(' ','').split('+')
    for i in range(0,len(wantto)):
        andlist = doandlist(wantto[i],allschool)#allschool#wantto[i]
        orlist.append(andlist)
    schoolset = set(orlist[0])
    for i in range(1,len(orlist)):#or not and!!#
        schoolset = schoolset | orlist[i]#and[i] is set##or#
    print(' '.join(list(sorted(schoolset))))#sorted##change list print#
    
