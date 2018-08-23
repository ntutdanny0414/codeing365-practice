class computer():
    def __init__(self,number,name):#self need#
        self.number = number
        self.name = name
    def legalnet(self):
        check = self.number.split('.')
        for i in range(0,len(check)):
            if int(check[i]) > 255:
                return False
        return True
    def getname(self):
        return self.name
    def getonetwo(self):
        one = self.number.split('.')
        return one[0]+'.'+one[1]
error = []
namenum = []
while True:
    data = input().split(',')
    if data[0] == '0.0.0.0' and data[1] == 'none':
        break
    else:
        s = computer(data[0],data[1])
        if s.legalnet():
            namenum.append([s.getname(),s.getonetwo()])
        else:
            error.append(s.getname())
outcome = []
while len(namenum) != 0:
    find = namenum[0][1]
    same = []
    for i in range(0,len(namenum)):
        if namenum[i][1] == find:
            same.append(namenum[i][0])
            namenum[i] = ''
    outcome.append(same)   
    while '' in namenum:
        namenum.remove('')
for i in range(0,len(outcome)):
    if len(outcome[i]) >= 2:
        alldata = outcome[i][0]
        for j in range(1,len(outcome[i])-1):#out[i]#
            alldata = alldata+', '+outcome[i][j]
        alldata = alldata +' and ' + outcome[i][-1]
        print('machines '+alldata+' are on the same local network.')
#    elif len(outcome[i]) == 2:
#        print('machines '+outcome[i][0]+' and '+outcome[i][1]+' are on the same local network.')
for i in range(0,len(error)):
    print('machine '+error[i]+' is error ip')
    
