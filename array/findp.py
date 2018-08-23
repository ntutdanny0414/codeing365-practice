def printbetween(english,count,word):
    english = english.lower()#way#
    word = word.lower()
    english = english.split(' ')
    find = []
    splitstring = []
    for i in range(0,len(english)):
        if english[i] == word:
            find.append(i)
    for i in range(0,len(find)):
        fromp = 0
        toq = 0
        every = []
        if find[i] - count < 0:
            fromp = 0
        else:
            fromp = find[i] - count
        if find[i] + count > len(english):
            toq = len(english)
        else:
            toq = find[i] + count + 1
        for j in range(fromp,toq):
            if j == find[i]:
                every.append(english[j].upper())
            else:
                every.append(english[j])
        splitstring.append(' '.join(every))
    return splitstring
def sort1(key):
    return key[0]
def sortway(unsort,word,LorR):
    key =  []
    if LorR == 'L':
        for i in range(0,len(unsort)):
            s = unsort[i].split(word.upper())[0].split()#way upper#
            s.reverse()
            key.append([''.join(s),unsort[i]])
        return sorted(key,key = sort1)
    elif LorR == 'R':
        for i in range(0,len(unsort)):
            s = unsort[i].split(word.upper())[1].split()
            key.append([''.join(s),unsort[i]])
        return sorted(key,key = sort1)
    
x = input().split(' ')
english = input()
unsort = printbetween(english,int(x[1]),x[0])
outcome = sortway(unsort,x[0],x[2])
for i in range(0,len(outcome)):
    print(outcome[i][1])
            
        
