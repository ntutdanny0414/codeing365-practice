v1 = input()
v1 = v1.split(' ')
color = []
v = []
for i in range(0,len(v1)):
    color.append(v1[i][-1])
    if len(v1[i]) == 3:
        v.append(int(v1[i][0]+v1[i][1]))
    elif len(v1[i]) == 2:
        v.append(int(v1[i][0]))
#    v[i] = v[i].replace(v[i][-1],'')
def judge(poker,r):
    two = []
    for i in poker:
        if poker.count(i) == r:
            two.append(i)
    return two
def Straight(poker):
    if (max(poker)-min(poker))==4 and len(set(poker))==5:
        return True

#def Straight2(poker):
#    poker.sort()
#    if (max(poker)-min(poker))==4 and len(set(poker))==5:
#        return  True
#    elif poker == [1,2,3,4,13]:
#        return True
if len(judge(v,2)) == 2 and len(judge(v,1)) == 3:
    print(1)
elif len(judge(v,2)) == 4 and len(judge(v,1)) == 1:
    print(2)
elif len(judge(v,3)) == 3 and len(judge(v,1)) == 2:
    print(3)
elif len(judge(v,3)) == 3 and len(judge(v,2)) == 2:
    print(4)
elif len(judge(v,4)) == 4 and len(judge(v,1)) == 1:
    print(5)
elif Straight(v) and len(set(color)) == 1:
    print(7)
elif Straight(v) or sorted(v) == [1,2,3,4,13]:
    print(6)

else:
    print(0)
