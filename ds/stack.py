def printdata(data):
    print(' '.join(str(e) for e in data))
data = []
sorc = input()
if sorc == '1':
    while True:
        smalldata = input().split(' ')
        if smalldata[0] == '1':
            if len(data) >= 5:
                print('FULL')
                break#stop#
            else:
                data.append(smalldata[1])
        elif smalldata[0] == '2':
            if len(data) == 0:
                print("EMPTY")
                break#stop#
            else:
                data.pop()#notfirst#
        elif smalldata[0] == '3':
            printdata(data)
            break
elif sorc == '2':
    while True:
        smalldata = input().split(' ')
        if smalldata[0] == '1':
            if len(data) >= 4:#can"t = 5 (remove)#
                print('FULL')
                break#stop#
            else:
                data.append(smalldata[1])
        elif smalldata[0] == '2':
            if len(data) == 0:
                print("EMPTY")
                break#stop#
            else:
                data.pop(0)#popfirst#
        elif smalldata[0] == '3':
            printdata(data)
            break
