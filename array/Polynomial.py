def splitstring(stringx):
    if 'x^'in stringx:
        stringx = stringx.split('x^')
        if stringx[0]=='':
            stringx[0] = '1'
        if stringx[0]=='-':
            stringx[0] = '-1'
        return stringx
    elif 'x'in stringx:
        stringx = stringx.split('x')
        if stringx[0]=='':
            stringx[0] = '1'
        if stringx[0]=='-':
            stringx[0] = '-1'
        return [stringx[0],'1']
    else:
        return [stringx,'0']
def tolist(polystring):#re.split(r'[|+|-]',s)no#
    polystring = polystring.replace(' ','').replace('-','+-').lstrip('+').split('+')
    #first no + lstrip('+')#
    numberlist = []
    for i in range(0,len(polystring)):
        numberlist.append(splitstring(polystring[i]))
    for i in range(0,len(numberlist)):
        numberlist[i][0] = int(numberlist[i][0])
        numberlist[i][1] = int(numberlist[i][1])
    return numberlist
def plus(poly1 , poly2):
    outcomepoly = []
    index1 = 0
    index2 = 0
    while not index1 >= len(poly1) and not index2 >= len(poly2):#notnot#
        if poly1[index1][1] > poly2[index2][1]:
            power  = poly1[index1][1]
            coeff = poly1[index1][0]
            index1 = index1 + 1
        elif poly1[index1][1] < poly2[index2][1]:
            power  = poly2[index2][1]
            coeff = poly2[index2][0]
            index2 = index2 + 1
        else:
            power  = poly1[index1][1]
            coeff = poly1[index1][0] + poly2[index2][0]
            index1 = index1 + 1
            index2 = index2 + 1
        outcomepoly.append([coeff,power])
    while not index1 >= len(poly1):
        outcomepoly.append([poly1[index1][0], poly1[index1][1]])
        index1 = index1 + 1
    while not index2 >= len(poly2):
        outcomepoly.append([poly2[index2][0], poly2[index2][1]])
        index2 = index2 + 1
    return outcomepoly
def minus(poly1 , poly2):#0 none#
    outcomepoly = []
    index1 = 0
    index2 = 0
    while not index1 >= len(poly1) and not index2 >= len(poly2):#notnot#
        if poly1[index1][1] > poly2[index2][1]:
            power  = poly1[index1][1]
            coeff = poly1[index1][0]
            index1 = index1 + 1
        elif poly1[index1][1] < poly2[index2][1]:
            power  = poly2[index2][1]
            coeff = -poly2[index2][0]
            index2 = index2 + 1
        else:
            power  = poly1[index1][1]
            coeff = poly1[index1][0] - poly2[index2][0]
            index1 = index1 + 1
            index2 = index2 + 1
        outcomepoly.append([coeff,power])
    while not index1 >= len(poly1):
        outcomepoly.append([poly1[index1][0], poly1[index1][1]])
        index1 = index1 + 1
    while not index2 >= len(poly2):#0-(poly2)#
        outcomepoly.append([-poly2[index2][0], poly2[index2][1]])
        index2 = index2 + 1
    return outcomepoly
def mul1bit(poly1 , poly2one):
    onepoly = []
    index1 = 0
    while not index1 >= len(poly1):
        coeff = poly1[index1][0] * poly2one[0]
        power = poly1[index1][1] + poly2one[1]
        onepoly.append([coeff,power])
        index1 = index1 + 1
    return onepoly
def mul(poly1 , poly2):
    outcomepoly = []
    for i in range(len(poly2)-1,-1,-1):
        outcomepoly = plus(outcomepoly,mul1bit(poly1,poly2[i]))
    return outcomepoly
def stringcheck(polyone):
    if polyone[0] == 1 and polyone[1] == 0:
        return ['+ '+str(polyone[0]),str(polyone[1])]
    elif polyone[0] == -1 and polyone[1] == 0:
        return ['- '+str(abs(polyone[0])),str(polyone[1])]
    elif polyone[0] == 1:
        return ['+ ',str(polyone[1])]
    elif polyone[0] == -1:
        return ['- ',str(polyone[1])]
    elif polyone[0] < 0:
        return ['- '+str(abs(polyone[0])),str(polyone[1])]
    elif polyone[0] > 0:
        return ['+ '+str(polyone[0]),str(polyone[1])]
def tostring(outcomepoly):
    string = []
    outcome = ''
    for i in range(0,len(outcomepoly)):
        if outcomepoly[i][0] == 0:
            pass
        elif outcomepoly[i][1] == 0:
            string.append(stringcheck(outcomepoly[i])[0])
        elif outcomepoly[i][1] == 1:
            string.append(stringcheck(outcomepoly[i])[0]+'x')
        else:
            string.append(stringcheck(outcomepoly[i])[0]+'x^'+stringcheck(outcomepoly[i])[1])
    for i in range(0,len(string)):
        outcome = outcome +' '+ string[i]
    if outcome == '':
        outcome = '0'
    elif outcome[1] == '+':
        outcome = outcome.lstrip(' + ')
    elif outcome[1] == '-':
        outcome = '-'+outcome.lstrip(' - ')
    print(outcome)
def main():
    fun = input()
    poly1 = input()
    poly2 = input()
    polylist1 = tolist(poly1)
    polylist2 = tolist(poly2)
    if fun == '+':
        outcome = plus(polylist1 , polylist2)
    elif fun == '-':
        outcome = minus(polylist1 , polylist2)
    elif fun == '*':
        outcome = mul(polylist1 , polylist2)    
    tostring(outcome)

main()