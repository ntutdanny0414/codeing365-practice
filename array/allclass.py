def function1(data,smallfun,studentid):
    if smallfun == 1:
        ave = data[studentid][0] + data[studentid][1]
        return int(ave/2)
    elif smallfun == 2:
        return data[studentid][0]
    elif smallfun == 3:
        return data[studentid][1]
def function2(data,smallfun):
    avemax = 0
    csmax = 0
    pgmax = 0
    for i in data:
        if (data[i][0] + data[i][1])/2 > avemax:
            avemax = (data[i][0] + data[i][1])/2
        if data[i][0] > csmax:
            csmax = data[i][0]
        if data[i][1] > pgmax:
            pgmax = data[i][1]
    if smallfun == 1:
        return int(avemax)
    elif smallfun == 2:
        return csmax
    elif smallfun == 3:
        return pgmax
def function3(data,smallfun):
    avemin = 100
    csmin = 100#min == 0#
    pgmin = 100
    for i in data:
        if (data[i][0] + data[i][1])/2 < avemin:
            avemin = (data[i][0] + data[i][1])/2
        if data[i][0] < csmin:
            csmin = data[i][0]
        if data[i][1] < pgmin:
            pgmin = data[i][1]
    if smallfun == 1:
        return int(avemin)
    elif smallfun == 2:
        return csmin
    elif smallfun == 3:
        return pgmin
def sortway(x):
    return x[0]
def function4(data,smallfun):
    ave = []
    cs = []
    pg = []
    for i in data:
        if (data[i][0] + data[i][1])/2 < 60:
            ave.append([i,int((data[i][0] + data[i][1])/2)])
        if data[i][0] < 60:
            cs.append([i,data[i][0]])
        if data[i][1] < 60:
            pg.append([i,data[i][1]]) 
    if smallfun == 1:
        return sorted(ave,key = sortway)
    elif smallfun == 2:
        return sorted(cs,key = sortway)
    elif smallfun == 3:
        return sorted(pg,key = sortway)
def function5(data,smallfun):
    ave = []
    cs = []
    pg = []
    for i in data:
        if (data[i][0] + data[i][1])/2 > 60:
            ave.append([i,int((data[i][0] + data[i][1])/2)])
        if data[i][0] > 60:
            cs.append([i,data[i][0]])
        if data[i][1] > 60:
            pg.append([i,data[i][1]]) 
    if smallfun == 1:
        return sorted(ave,key = sortway)
    elif smallfun == 2:
        return sorted(cs,key = sortway)
    elif smallfun == 3:
        return sorted(pg,key = sortway)
def sortave(x):
    return (x[1][0]+x[1][1])/2
def sortcs(x):
    return x[1][0]
def sortpg(x):
    return x[1][1]
def function6(data,smallfun):
    data = list(data.items())
    sort = []
    if smallfun == 1:
        v = sorted(data,key = sortave,reverse = True)
        for i in range(0,3):
            ave = int((v[i][1][0] + v[i][1][1]) / 2)
            sort.append([v[i][0],ave])
        return sort
    elif smallfun == 2:
        v = sorted(data,key = sortcs,reverse = True)
        for i in range(0,3):
            cs = v[i][1][0]
            sort.append([v[i][0],cs])
        return sort
    elif smallfun == 3:
        v = sorted(data,key = sortpg,reverse = True)
        for i in range(0,3):
            pg = v[i][1][1]
            sort.append([v[i][0],pg])
        return sort
def function7(data,smallfun):#ave = v#
    v = []
    for i in data:
        v.append(int((data[i][0] + data[i][1])/2))
    v = sorted(v)
    if smallfun == 1:
        if len(v) % 2 == 1:
            med = int((len(v)-1)/2)
            return v[med]
        else:
            med = int(len(v)/2)
            return (v[med] + v[med-1]) / 2
    elif smallfun == 2:
        return function72(v)
def function72(v):
    score = []
    score.append('0-10:')
    score.append('11-20:')
    score.append('21-30:')
    score.append('31-40:')
    score.append('41-50:')
    score.append('51-60:')
    score.append('61-70:')
    score.append('71-80:')
    score.append('81-90:')
    score.append('91-100:')
    for i in range(0,len(v)):
        score[int((v[i]-1)/10)] = score[int((v[i]-1)/10)]+'*'
    return score

data = {}
while True:
    word = input()
    if word == '-1':
        break
    else:
        word = word.split(' ')
        data[int(word[0])] = [int(word[1]),int(word[2])]
bigfun = int(input())
smallfun = int(input())
if bigfun == 1:
    studentid = int(input())
    print(function1(data,smallfun,studentid))
elif bigfun == 2:
    print(function2(data,smallfun))
elif bigfun == 3:
    print(function3(data,smallfun))
elif bigfun == 4:
    under60 = function4(data,smallfun)
    for i in range(0,len(under60)):
        print(str(under60[i][0])+':'+str(under60[i][1]))
elif bigfun == 5:
    up60 = function5(data,smallfun)
    for i in range(0,len(up60)):
        print(str(up60[i][0])+':'+str(up60[i][1]))
elif bigfun == 6:
    prize = function6(data,smallfun)
    print('1st:'+str(prize[0][0])+' '+str(prize[0][1]))
    print('2nd:'+str(prize[1][0])+' '+str(prize[1][1]))
    print('3rd:'+str(prize[2][0])+' '+str(prize[2][1]))
elif bigfun == 7:
    if smallfun == 1:
        print(function7(data,smallfun))
    elif smallfun == 2:
        graph = function7(data,smallfun)
        for i in range(0,len(graph)):
            print(graph[i])
