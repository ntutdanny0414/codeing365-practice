data = {}
def sort(string):
    strl = string[:1]
    strr = string[1:]
    strr = sorted(strr)#list#
    return [strl,''.join(strr)]
#def insert(out,key,string):
#    for i in range(len(string)-1,-1,-1):
#        out.insert(out.index(key)+1,string[i])#index#
def dicprint(data):#list#
    data = list(data.items())
    out = []
    out.append(data[0][0])
    for i in range(0,len(data[0][1])):#0#
        out.append(data[0][1][i])
    for i in range(1,len(data)):
        for j in range(len(data[i][1])-1,-1,-1):
            out.insert(out.index(data[i][0])+1,data[i][1][j])#ij#
    return out
while True:
    want = input()
    if want == 'p':
        if len(data)==0:
            print('null')
        else:
            print(''.join(dicprint(data)))
    elif want == 'i':
        string = input()
        strsort = sort(string)
        if strsort[0] in data:
            data[strsort[0]] = data[strsort[0]] + strsort[1]
            data[strsort[0]] = ''.join(sorted(data[strsort[0]]))#list string#
        else:
            data[strsort[0]] = strsort[1]
    elif want == 'e':
        break