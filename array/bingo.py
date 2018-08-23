outcome = []
def check(match):
    if len(set(match)&set([0,1,2])) == 3:
        return True
    elif len(set(match)&set([3,4,5])) == 3:
        return True
    elif len(set(match)&set([6,7,8])) == 3:
        return True
    elif len(set(match)&set([0,3,6])) == 3:
        return True
    elif len(set(match)&set([1,4,7])) == 3:
        return True
    elif len(set(match)&set([2,5,8])) == 3:
        return True
    elif len(set(match)&set([0,4,8])) == 3:
        return True
    elif len(set(match)&set([2,4,6])) == 3:
        return True
    else:
        return False
    
while True:
    v1 = input()
    v2 = input()
    com = input()
    p1 = v1.split(' ')
    p2 = v2.split(' ')
    co = com.split(' ')
    match1 = []
    match2 = []
    for i in range(0,3):
        match1.append(p1.index(co[i]))#List.index( '??' )
        match2.append(p2.index(co[i]))
    if check(match1) == True and check(match2) == False:
        outcome.append('Player1 wins')
    elif check(match1) == False and check(match2) == True:
        outcome.append('Player2 wins')
    elif check(match1) == True and check(match2) == True:
        outcome.append('Draw')
    elif check(match1) == False and check(match2) == False:
        outcome.append('Draw')
    nex = int(input())
    if nex == -1:
        break
for i in range(0,len(outcome)):
    print(outcome[i])
