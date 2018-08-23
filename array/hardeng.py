pr2 = []
pr3 = []
pr4 = []
pr1 = input()
pr = pr1.split(' ')
for i in range(0,len(pr)):
    pr2.append(pr[i])
    pr3.append(pr[i])
    pr4.append(pr[i])
w1 = input()
w2 = input()
def replace(listv):
    for i in range(0,len(listv)):
        if listv[i] == w1:
            listv[i] = w2
    print(' '.join(listv))
def insert(listv):
    for i in range(0,len(listv)):
        if listv[i] == w1:
            listv[i] = w2 + ' ' + w1
    print(' '.join(listv))
def remove(listv):
    for i in range(0,len(listv)):
        if listv[i] == w1:
            listv[i] = ' '
    while ' ' in listv:##
        listv.remove(' ')
    print(' '.join(listv))
def sort(listv):
    d = {x:listv.count(x) for x in listv}
    sorted_by_value = sorted(d.items(), key=lambda kv: kv[0])
    maxv = sorted_by_value[0][1]
    for i in range(0,len(sorted_by_value)):
        if sorted_by_value[i][1]>maxv:
            maxv = sorted_by_value[i][1]
    for i in range(0,len(sorted_by_value)):
        sorted_by_value[i] = list(sorted_by_value[i])
    for i in range(maxv , 0,-1):
        for j in range(0,len(sorted_by_value)):
            if sorted_by_value[j][1] == i:
                sorted_by_value[j][1] = str(sorted_by_value[j][1])
                print(' '.join(sorted_by_value[j]))

replace(pr)
insert(pr2)
remove(pr3)
sort(pr4)