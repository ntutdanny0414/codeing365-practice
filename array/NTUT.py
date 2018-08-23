x = int(input())
twoitem = []
for i in range(0,x):
    x = input().split(',')
    for j in range(0,len(x)-1):
        for k in range(j+1,len(x)):
            if int(x[j]) >= int(x[k]):#int  change#
                twoitem.append(x[k]+','+x[j])
            else:
                twoitem.append(x[j]+','+x[k])
sort = {x:twoitem.count(x) for x in twoitem}#not i#
def sortway(n):
    return n[1]
sort = list(sort.items())
sort = sorted(sort,key = sortway,reverse = True)#dictionary no repeat key#
print(sort[0][0]+','+str(sort[0][1]))#sort[0]big#
