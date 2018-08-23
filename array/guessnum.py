def checkA(number,allnumber,match):
    count = 0
    for i in range(0,4):
        if number[i] == allnumber[i]:
            count = count + 1
    return count == match
def checkB(number,allnumber,match):
    count = 0
    for i in range(0,4):#range#
        for j in range(0,4):
            if i == j:
                pass
            elif number[i] == allnumber[j]:
                count = count + 1
    return count == match
def clear(allnumber,clear):
    while clear in allnumber:
        allnumber.remove(clear)
def main():
    allnumber = []
    for i in range(102,9877):
        if len(str(i)) == 4 and len(set(str(i))) == 4:#setfindrepeat#
            allnumber.append(str(i))
        elif len(str(i)) == 3 and len(set('0'+str(i))) == 4:#len(set())==4not set()==4#
            allnumber.append('0'+str(i))
    while len(allnumber) != 1:
        data = input().split(',')
        matchA = int(data[1][0])#2a2b#
        matchB = int(data[1][2])#intint!!#
        for i in range(0,len(allnumber)):
            if not (checkA(data[0],allnumber[i],matchA) and checkB(data[0],allnumber[i],matchB)):
                allnumber[i] = ' '
        clear(allnumber,' ')
    print(allnumber[0])
main()
        
                