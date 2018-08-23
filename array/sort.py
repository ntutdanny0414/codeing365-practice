def bubble(alist):
    count = 0
    for i in range(0, len(alist)-1):
        for j in range(0, len(alist)-1-i):
            if alist[j] > alist[j+1]:
                flag = True
                alist[j] , alist[j+1] = alist[j+1] , alist[j]
                count = count + 1
    print(' '.join(str(e) for e in alist))
    print('Bubble Sort change times =',count)
def insertion(alist):
    count = 0
    for i in range(1, len(alist)):
        tmp = alist[i]
        j = i - 1
        while j >= 0 and tmp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
            count = count + 1
        alist[ j + 1 ] = tmp
    print('Insertion Sort change times =',count)
def selection(alist):
    count = 0
    for i in range(0, len(alist)-1):
        minindx = i
        for j in range(i+1, len(alist)):
            if (alist[minindx] > alist[j]):
                minindx = j
        if (minindx!=i):
            tmp = alist[minindx]
            alist[minindx] = alist[i]
            alist[i] = tmp
            count = count + 1
    print('Selection Sort change times =',count)
def bubble1(alist):
    count = 0
    for i in range(0, len(alist)-1):
        flag = False
        for j in range(0, len(alist)-1-i):
            if alist[j] < alist[j+1]:
                flag = True
                alist[j] , alist[j+1] = alist[j+1] , alist[j]
                count = count + 1
        if flag == False:
            break        
    print(' '.join(str(e) for e in alist))
    print('Bubble Sort change times =',count)

def insertion1(alist):
    count = 0
    for i in range(1, len(alist)):
        tmp = alist[i]
        j = i - 1
        while j >= 0 and tmp > alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
            count = count + 1
        alist[ j + 1 ] = tmp
    print('Insertion Sort change times =',count)
def selection1(alist):
    count = 0
    for i in range(0, len(alist)-1):
        minindx = i
        for j in range(i+1, len(alist)):
            if (alist[minindx] < alist[j]):
                minindx = j
        if (minindx!=i):
            tmp = alist[minindx]
            alist[minindx] = alist[i]
            alist[i] = tmp
            count = count + 1
    print('Selection Sort change times =',count)
v = input()
way = int(input())
alist = v.split(' ')
alist.pop()
alist1 = []
alist2 = []
for i in range(0,len(alist)):
    alist[i] = int(alist[i])
    alist1.append(alist[i])
    alist2.append(alist[i])
if way == 0:
    bubble(alist)
    insertion(alist1)
    selection(alist2)
elif way == 1:
    bubble1(alist)
    insertion1(alist1)
    selection1(alist2)    
