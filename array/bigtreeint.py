def plus(input1,input2):
    number1 = []
    number2 = []
    for i in range(len(input1)-1,-1,-1):
        number1.append(int(input1[i]))
    for i in range(len(input2)-1,-1,-1):
        number2.append(int(input2[i]))
    plus = []
    if len(number1) >= len(number2):
        for i in range(0,len(number2)):
            plus.append(number1[i]+number2[i])
        for i in range(len(number2),len(number1)):
            plus.append(number1[i])
    else:
        for i in range(0,len(number1)):
            plus.append(number1[i]+number2[i])
        for i in range(len(number1),len(number2)):
            plus.append(number2[i])
    for i in range(0,len(plus)-1):
        if plus[i] >=10:
            plus[i+1] = plus[i+1] + (plus[i]//10)#first#
            plus[i] = plus[i] % 10
        else:
            plus[i] = plus[i]
    plus.reverse()
    return ''.join(str(i) for i in plus)
    
def minus(input1,input2):
    number1 = []
    number2 = []
    for i in range(len(input1)-1,-1,-1):
        number1.append(int(input1[i]))
    for i in range(len(input2)-1,-1,-1):
        number2.append(int(input2[i]))
    minus = []
    if len(number1) >= len(number2):
        while len(number2) != len(number1):
            number2.append(0)
    else:
        while len(number1) != len(number2):
            number1.append(0)    
    for i in range(0,len(number1)):
        minus.append(number1[i]-number2[i])
    for i in range(0,len(minus)-1):
        if minus[i] < 0:
            minus[i+1] = minus[i+1] - 1#first#
            minus[i] = minus[i] + 10
        else:
            minus[i] = minus[i]
    minus.reverse()
    return ''.join(str(i) for i in minus)

def checkminus(input1,input2):##
    if int(input1) < int(input2):
        return '-'+minus(input2,input1)
    else:
        return minus(input1,input2)
def mul_1_bit(number1,bit):
    mul_1 = []
    for i in range(0,len(number1)):
        mul_1.append(number1[i] * bit)
    for i in range(0,len(mul_1)-1):
        if mul_1[i] >= 10:
            mul_1[i+1] = mul_1[i+1] + (mul_1[i]//10)
            mul_1[i] = mul_1[i] % 10
        else:
            mul_1[i] = mul_1[i]
    mul_1.reverse()
    return ''.join(str(i) for i in mul_1)

def mul(input1,input2):
    number1 = []
    number2 = []
    for i in range(len(input1)-1,-1,-1):
        number1.append(int(input1[i]))
    for i in range(len(input2)-1,-1,-1):
        number2.append(int(input2[i]))
    mul = mul_1_bit(number1,number2[0])
    ten = ''
    for i in range(1,len(number2)):
        ten = ten + '0'
        mulnext = mul_1_bit(number1,number2[i]) + ten
        mul = plus(mul,mulnext)
    return mul
def check(number):
    check = number.lstrip('-').lstrip('0')
    if check == '':
        return '0'
    elif number[0] == '-' and number[1] == '-':
        return check
    elif number[0] == '-':
        return '-'+ check
    else:
        return check
input1 = input()
input2 = input()
if input1[0] != '-'and input2[0] != '-':
    print(check(plus(input1,input2)))
    print(check(minus(input1,input2)))
    print(check(mul(input1,input2)))
elif input1[0] == '-'and input2[0] != '-':
    input1 = input1.lstrip('-')#a[0]xx#
    print(check(minus(input2,input1)))
    print(check('-'+plus(input1,input2)))
    print(check('-'+mul(input1,input2)))
elif input1[0] != '-'and input2[0] == '-':
    input2 = input2.lstrip('-')#a[0]xx#
    print(check(minus(input1,input2)))
    print(check(plus(input1,input2)))
    print(check('-'+mul(input1,input2)))
elif input1[0] == '-'and input2[0] == '-':
    input1 = input1.lstrip('-')
    input2 = input2.lstrip('-')   
    print(check('-'+plus(input1,input2)))
    print(check('-'+minus(input2,input1)))
    print(check(mul(input1,input2)))   
