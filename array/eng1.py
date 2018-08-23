worddata = []
subword = []
while True:
    word = input()
    if word == '-1':
        break
    worddata.append(word)
para = input().split()
for i in range(0,len(para)):
    if para[i] not in worddata:
        subword.append(para[i])
        para[i] = ' '
while ' ' in para:#
    para.remove(' ')#
print(' '.join(subword))
print(len(subword))
count = {x:para.count(x) for x in para}##
def sort(x):
    return x[0].lower()#A=a#
count = list(count.items())
sorted_by_value = sorted(count, key= sort)
maxc = sorted_by_value[0][1]
for i in range(0,len(sorted_by_value)):
    if sorted_by_value[i][1]>maxc:
        maxc = sorted_by_value[i][1]
for i in range(0,len(sorted_by_value)):
    sorted_by_value[i] = list(sorted_by_value[i])#canchange#
for i in range(maxc , 0,-1):#to1#
    for j in range(0,len(sorted_by_value)):
        if sorted_by_value[j][1] == i:
            sorted_by_value[j][1] = str(sorted_by_value[j][1])
            print(' '.join(sorted_by_value[j]))

        
