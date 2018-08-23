order1 = input()
data1 = input()
order2 = input()
data2 = input()
outdata = []
def splitpi(pre,ino,out = []):#append two#
    if len(pre) == 0:
        outdata.append(out)
    elif len(pre) == 1:
        splitpi('','',out)
    elif len(pre) == 2:
        out.append(pre[1])
        i = ino[ino.index(pre[0])-1]
        splitpi(pre[1],i,out)#0>1#
    else:
        ileft = ino[:ino.index(pre[0])]
        iright = ino[ino.index(pre[0])+1:]
        pleft = pre[1:pre.index(ileft[-1])+1]#index#
        pright = pre[pre.index(ileft[-1])+1:]#main#
        out.append(pleft[0])
        out.append(pright[0])
        splitpi(pleft,ileft,out)
        splitpi(pright,iright,out)
def splitoi(post,ino,out = []):
    if len(post) == 0:
        outdata.append(out)
    elif len(post) == 1:
        splitpi('','',out)
    elif len(post) == 2:
        out.append(post[1])
        i = ino[ino.index(post[0])-1]
        splitpi(post[1],i,out)#0>1#
    else:
        ileft = ino[:ino.index(post[0])]
        iright = ino[ino.index(post[0])+1:]
        pleft = ''
        pright = ''
        for i in range(0,len(post)):
            if post[i] in ileft:
                pleft += post[i]
            if post[i] in iright:
                pright += post[i]
        out.append(pleft[0])
        out.append(pright[0])
        splitoi(pleft,ileft,out)#remember#
        splitoi(pright,iright,out)
if order1 == 'P':
    splitpi(data1,data2,[data1[0]])
    print(''.join(outdata[-1]))
elif order2 == 'P':
    splitpi(data2,data1,[data2[0]])
    print(''.join(outdata[-1]))
elif order1 =='O':
    re = []#REVERSE#
    for i in range(len(data1)-1,-1,-1):
        re.append(data1[i])
    data1 = ''.join(re)
    splitoi(data1,data2,[data1[0]])
    print(''.join(outdata[-1]))
elif order2 == 'O':
    re = []
    for i in range(len(data2)-1,-1,-1):
        re.append(data2[i])
    data2 = ''.join(re)
    splitoi(data2,data1,[data2[0]])
    print(''.join(outdata[-1]))
