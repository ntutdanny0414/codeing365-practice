size = int(input())
data = []

for i in range(size):
    row = input().split()
    data.append(row)
def allpath(point,path):
    goto = [(1,0),(-1,0),(0,-1),(0,1)]
    if point == (size-2,size-2):#name size#
        path.append((size-2,size-2))
        return path
    for i in goto:
        if data[point[0]+i[0]][point[1]+i[1]] == '0':#0>1#
            if (point[0]+i[0],point[1]+i[1])in path:#()in#
                pass
            else:
                path.append(point)#need copy#
                nextpath = path.copy()
                nextdata = allpath((point[0]+i[0],point[1]+i[1]),nextpath)#def name and path same#
                if nextdata != False:
                    return nextdata
    return False
#list call defname and list name same#
change = allpath((1,1),[])
for i in change:
    data[i[0]][i[1]] = '#'
for i in range(0,size):
    print(' '.join(data[i]))

