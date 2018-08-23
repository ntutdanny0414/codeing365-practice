outcome = []
a = []
b = []
while True:
    function = input()
    function = function.split(' ')
    for i in range(0,len(function)):
        function[i] = int(function[i])
    if function[0] == 0:
        break
    elif function[0] == 1:
        a = []
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)
    elif function[0] == 2:
        b = []
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)    
    elif function[0] == 3:
        if function[1] not in a:
            a.append(function[1])
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)
    elif function[0] == 4:
        if function[1] not in b:
            b.append(function[1])
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)
    elif function[0] == 5:
        a.remove(function[1])
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)
    elif function[0] == 6:
        b.remove(function[1])
        word = 'A:['+''.join(str(e)+',' for e in a)+']'+ 'B:['+''.join(str(e)+',' for e in b)+']'
        outcome.append(word)
    elif function[0] == 7:
        andset = sorted(list(set(a)|set(b)))
        word = '['+''.join(str(e)+',' for e in andset)+']'
        outcome.append(word)
    elif function[0] == 8:
        andset = sorted(list(set(a)&set(b)))#key == a.index#
        word = '['+''.join(str(e)+',' for e in andset)+']'
        outcome.append(word)
    elif function[0] == 9:
        if set(a).issubset(set(b)):#set(a)<=set(b)
            outcome.append('1')
        else:
            outcome.append('0')
for i in range(0,len(outcome)):
    print(outcome[i])
